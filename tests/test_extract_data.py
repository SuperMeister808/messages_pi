
import unittest
from unittest.mock import patch

from server import Server

from message import CollectMessage
from title import CollectTitel

class TestExtractData(unittest.TestCase):

    def setUp(self):
        
        self.server = Server("Testing...", "Testing...")

        self.test_client = self.server.app.test_client()

    def test_correct_json_format(self):

        data = {"title": "title", "message": "message"}

        with patch.object(Server, "clear_data") as clear:

            response = self.test_client.post("/send", json=data)

            clear.assert_called_once()
            
            self.assertEqual(response.json, {"Success": "Thanks for you request!"})
            self.assertEqual(response.status_code, 200)
        
            result_title = CollectTitel.titels[-1]
            result_message = CollectMessage.messages[-1]

            self.assertEqual(result_title.title , "title")
            self.assertEqual(result_message.message , "message")

            CollectTitel.clear_titles()
            CollectMessage.clear_messages()

if __name__ == "__main__":

    unittest.main()

