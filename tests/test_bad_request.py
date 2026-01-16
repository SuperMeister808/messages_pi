
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
        
        with patch.object(Server, "extract_data", return_value=("titel", "message")) as extract:

            with patch.object(Server, "collect_data") as collect:

                with patch.object(Server, "clear_data") as clear:

                    response = self.test_client.post("/send", json=data)

                    extract.assert_called_once()
                    collect.assert_called_once()
                    clear.assert_called_once()
                    
                    self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                    self.assertEqual(response.status_code, 200)

    def test_bad_request(self):

        data = {"test": "test"}
        
        with patch.object(Server, "extract_data", return_value=("titel", "message")) as extract:

            with patch.object(Server, "collect_data") as collect:

                with patch.object(Server, "clear_data") as clear:

                    response = self.test_client.post("/send", data=data, content_type="application/json")
                    
                    extract.assert_not_called()
                    collect.assert_not_called()
                    clear.assert_not_called()
                    
                    self.assertEqual(response.json, {"Error": "Bad Request"})
                    self.assertEqual(response.status_code, 400)

if __name__ == "__main__":

    unittest.main()