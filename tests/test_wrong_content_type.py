
import unittest
from unittest.mock import patch

from server import Server

import io

class TestWrongContentType(unittest.TestCase):

    def setUp(self):
        
        self.server = Server("Testing...", "Testing...")
        self.test_client = self.server.app.test_client()

    def test_right_content_type(self):

            data = {"test": "test"}
        
            with patch.object(Server, "extract_data") as extract:
                with patch("sqlite3.connect", return_value="not relevant") as connection:
                    with patch.object(Server, "close_connection") as clear_connection:
                        with patch.object(Server, "clear_data") as clear_data:

                            response = self.test_client.post("/send", json=data)

                            extract.assert_called_once()
                            clear_data.assert_called_once()
                            connection.assert_called_once()
                            clear_connection.assert_called_once()

                            self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                            self.assertEqual(response.status_code, 200)

    def test_wrong_content_type(self):

            data = {"test": (io.BytesIO(b"Testing..."), "test.pdf")}
        
            with patch.object(Server, "extract_data") as extract:
                with patch("sqlite3.connect", return_value="not relevant") as connection:
                    with patch.object(Server, "close_connection") as clear_connection:
                        with patch.object(Server, "clear_data") as clear_data:

                            response = self.test_client.post("/send", data=data, headers={"Content-Type": "multipart/form-data"})

                            connection.assert_called_once()
                            clear_connection.assert_called_once()

                            self.assertEqual(response.json, {"Error": "Content Type application/json not found!"})
                            self.assertEqual(response.status_code, 405)

if __name__ == "__main__":

    unittest.main()