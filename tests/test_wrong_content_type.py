
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
        
            with patch.object(Server, "extract_data", return_value=("t", "m")) as extract:
                with patch.object(Server, "collect_data") as collect:
                    with patch.object(Server, "write_data") as write:
                        with patch("sqlite3.connect", return_value="not relevant") as connection:
                            with patch.object(Server, "close_connection") as close:
                                with patch.object(Server, "clear_data") as clear:

                                    response = self.test_client.post("/send", json=data)

                                    extract.assert_called_once()
                                    collect.assert_called_once()
                                    write.assert_called_once()
                                    connection.assert_called_once()
                                    close.assert_called_once()
                                    clear.assert_called_once()

                                    self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                                    self.assertEqual(response.status_code, 200)

    def test_wrong_content_type(self):

                data = {"test": (io.BytesIO(b"Testing..."), "test.pdf")}
        
            
                with patch.object(Server, "extract_data", return_value=("t", "m")) as extract:
                    with patch.object(Server, "collect_data") as collect:
                        with patch.object(Server, "write_data") as write:
                            with patch("sqlite3.connect", return_value="not relevant") as connection:
                                with patch.object(Server, "close_connection") as close:
                                    with patch.object(Server, "clear_data") as clear:
                                        response = self.test_client.post("/send", data=data, headers={"Content-Type": "multipart/form-data"})

                                        connection.assert_called_once()
                                        close.assert_called_once()
                                        extract.assert_not_called()
                                        collect.assert_not_called()
                                        write.assert_not_called()
                                        clear.assert_called_once()

                                        self.assertEqual(response.json, {"Error": "Content Type application/json not found!"})
                                        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":

    unittest.main()