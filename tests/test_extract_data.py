
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

        data = {"titel": "titel", "message": "message"}

        with patch.object(Server, "clear_data") as clear:

            with patch.object(Server, "write_data_on_database") as database:
            
                response = self.test_client.post("/send", json=data)

                database.assert_called_once()
                clear.assert_called_once()
            
                self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                self.assertEqual(response.status_code, 200)
        
                result_title = CollectTitel.titels[-1]
                result_message = CollectMessage.messages[-1]

                self.assertEqual(result_title.titel , "titel")
                self.assertEqual(result_message.message , "message")

                CollectTitel.clear_titles()
                CollectMessage.clear_messages()

    def test_less_keys(self):

        data = {"titel": "titel"}

        response = self.test_client.post("/send", json=data)
            
        self.assertEqual(response.json, {"Error": "Keys not found"})
        self.assertEqual(response.status_code, 405)
        
        result_titles = CollectTitel.titels
        result_messages = CollectMessage.messages

        self.assertEqual(len(result_titles) , 0)
        self.assertEqual(len(result_messages) , 0)


    def test_wrong_key(self):

        data = {"titel": "titel", "letter": "letter"}

        response = self.test_client.post("/send", json=data)
            
        self.assertEqual(response.json, {"Error": "Keys not found"})
        self.assertEqual(response.status_code, 405)
        
        result_titles = CollectTitel.titels
        result_messages = CollectMessage.messages

        self.assertEqual(len(result_titles) , 0)
        self.assertEqual(len(result_messages) , 0)

    def test_extra_key(self):

        data = {"titel": "titel", "message": "message", "extra": "extra"}

        with patch.object(Server, "clear_data") as clear:
        
            with patch.object(Server, "write_data_on_database") as database:
            
                response = self.test_client.post("/send", json=data)
            
                database.assert_called_once()
                clear.assert_called_once()
            
                self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                self.assertEqual(response.status_code, 200)
        
                result_titles = CollectTitel.titels
                result_messages = CollectMessage.messages

                self.assertEqual(result_titles[-1].titel , "titel")
                self.assertEqual(result_messages[-1].message , "message")

                CollectTitel.clear_titles()
                CollectMessage.clear_messages()

if __name__ == "__main__":

    unittest.main()

