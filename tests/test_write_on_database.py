
import unittest
from unittest.mock import patch

from server import Server
from database import Database

class TestWriteOnDatabase(unittest.TestCase):

    def setUp(self):

        self.server = Server("Testing...", "Testing...")
        self.test_client = self.server.app.test_client()

    def test_call_write_on_database(self):

        data = {"titel": "titel", "message": "message"}
        
        with patch.object(Database, "connect_to_database") as connect:

            with patch.object(Database, "add_message") as add:

                response = self.test_client.post("/send", json=data)  

                connect.assert_called_once()
                add.assert_called_once()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"Success": "Thanks for you request!"})     

if __name__ == "__main__":

    unittest.main()