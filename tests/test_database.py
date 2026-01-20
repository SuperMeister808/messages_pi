
import unittest
from unittest.mock import patch

from server import Server
from title import CollectTitel
from message import CollectMessage

import sqlite3

class TestDatabase(unittest.TestCase):

    def setUp(self):
        
        self.server = Server("Testing...", "Testing...")
        self.test_client = self.server.app.test_client()
    
    def test_correct_arguments(self):

            data = {"titel": "Greet", "message": "Hello World!"}

            conn = sqlite3.connect(":memory:")

            with patch("sqlite3.connect", return_value=conn) as connect:
                with patch.object(Server, "extract_data", return_value=("t", "m")) as extract_data:
                    with patch.object(Server, "collect_data") as collect:
                        with patch.object(CollectTitel, "titels", [CollectTitel.Titel(data["titel"])]):
                            with patch.object(CollectMessage, "messages", [CollectMessage.Message(data["message"])]):
                                with patch.object(Server, "close_connection") as close:
                        

                                    response = self.test_client.post("/send", json=data, environ_base={"conn": conn})

                                    self.assertEqual(response.status_code, 200)
                                    self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                        
                                    connect.assert_called_once()
                                    extract_data.assert_called_once()
                                    collect.assert_called_once()
                                    close.assert_called_once()

                                    cursor = conn.cursor()

                                    cursor.execute("SELECT * FROM messages")
                                    colums = [desc[0] for desc in cursor.description]
                                    rows = cursor.fetchall()

                                    self.assertEqual(colums, ["titel", "message"])
                                    self.assertEqual(rows, [("Greet", "Hello World!")])

            conn.close()  
    
if __name__ == "__main__":

    unittest.main()
    