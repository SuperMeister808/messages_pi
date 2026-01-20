
import unittest
from unittest.mock import patch

from server import Server

import io

class TestBadRequest(unittest.TestCase):

    def setUp(self):

        self.server = Server("Testing...", "Testing...")
        self.test_client = self.server.app.test_client()

    def test_correct_reequest(self):

        data = {"test": "test"}
        
        with patch("sqlite3.connect", return_value="not relevant") as connection:
            with patch.object(Server, "close_connection") as close_connection:
                with patch.object(Server, "extract_data") as extract:
                    with patch.object(Server, "clear_data") as clear_data:
                    
                        response = self.test_client.post("/send", json=data)

                        connection.assert_called_once()
                        close_connection.assert_called_once()
                        extract.assert_called_once()
                        clear_data.assert_called_once()
                    
                        self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                        self.assertEqual(response.status_code, 200)

    def test_bad_request(self):

        data = {"test": "test"}
        
        with patch("sqlite3.connect", return_value="not relevant") as connection:
            with patch.object(Server, "close_connection") as close_connection:
                with patch.object(Server, "extract_data") as extract:
                    with patch.object(Server, "clear_data") as clear_data:

                        response = self.test_client.post("/send", data=data, content_type="application/json")
                    
                        connection.assert_called_once()
                        close_connection.assert_called_once()
                    
                        self.assertEqual(response.json, {"Error": "Bad Request"})
                        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":

    unittest.main()