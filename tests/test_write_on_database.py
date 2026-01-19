
import unittest
from unittest.mock import patch

from server import Server
from database import Database
from connections import CollectConnections

import sqlite3

class TestWriteOnDatabase(unittest.TestCase):

    def setUp(self):

        self.server = Server("Testing...", "Testing...")
        self.test_client = self.server.app.test_client()

    def test_call_write_on_database(self):

        data = {"titel": "titel", "message": "message"}
        
        with patch.object(Database, "create_table"):

            with patch.object(Database, "add_message") as add:

                response = self.test_client.post("/send", json=data)  
                
                add.assert_called_once()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"Success": "Thanks for you request!"})     

    def test_write_on_database_correct_request(self):

        data = {"titel": "Test", "message": "This is a test"}

        original_connect = sqlite3.connect
        
        with patch("sqlite3.connect", side_effect=lambda _:original_connect(":memory:")) as connect:

            with patch.object(CollectConnections, "clear_connections") as clear:
            
                response = self.test_client.post("/send", json=data)

                #connect.assert_called_once()
                #clear.assert_called_once()
                
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"Success": "Thanks for you request!"})

                c = CollectConnections.connections[-1]
                conn = c.connection

                cursor = conn.cursor()
                cursor.execute("SELECT * FROM messages")

                colums = [desc[0] for desc in cursor.description]
                
                rows = cursor.fetchall()
                
                self.assertEqual(colums, ['titel', 'message'])
                self.assertEqual(rows, [("Test", "This is a test")])

                CollectConnections.clear_connections()
                
                conn.close()


if __name__ == "__main__":

    unittest.main()