
import unittest
from unittest.mock import patch

from server import Server
from database import Database

import sqlite3

class TestDatabase(unittest.TestCase):

    def setUp(self):
        
        self.server = Server("Testing...", "Testing...")
        self.test_client = self.server.app.test_client()
    
    def test_correct_arguments(self):

            data = {"title": "Greet", "message": "Hello World!"}

            conn = sqlite3.connect(":memory:")

            with patch("sqlite3.connect", return_value=conn) as connection:
                with patch.object(Server, "close_connection") as close:
                    with patch.object(Server, "extract_data", return_value=(data["title"], data["message"])) as extract:
                        with patch.object(Server, "collect_data") as collect:
                            with patch.object(Server, "clear_data") as clear:
                        

                                response = self.test_client.post("/send", json=data)

                                self.assertEqual(response.status_code, 200)
                                self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                        
                                connection.assert_called_once()
                                collect.assert_called_once()
                                clear.assert_called_once()
                                close.assert_called_once()
                                extract.assert_called_once()

                                cursor = conn.cursor()

                                cursor.execute("SELECT * FROM messages")
                                colums = [desc[0] for desc in cursor.description]
                                rows = cursor.fetchall()

                                self.assertEqual(colums, ["title", "message"])
                                self.assertEqual(rows, [("Greet", "Hello World!")])

            conn.close()  

    def test_broken_database(self):

        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()

        data = {"title": "title", "message": "message"}

        with patch("sqlite3.connect", return_value=conn) as connection:
            with patch.object(Server, "close_connection") as close:
                with patch.object(Server, "extract_data", return_value=(data["title"], data["message"])) as extract:
                    with patch.object(Server, "collect_data") as collect:
                        with patch.object(Server, "clear_data") as clear:
                            with patch.object(Database, "create_table") as table:

                                response = self.test_client.post("/send", json=data)

                                self.assertEqual(response.status_code, 500)
                                self.assertEqual(response.json, {"Error": "Table not found!"})
                        
                                connection.assert_called_once()
                                collect.assert_called_once()
                                extract.assert_called_once()
                                table.assert_called_once()
                                clear.assert_called_once()
                                close.assert_called_once()

        conn.close()


                                     
    
if __name__ == "__main__":

    unittest.main()
    