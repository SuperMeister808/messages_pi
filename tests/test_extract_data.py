
import unittest
from unittest.mock import patch

from server import Server
from message_handler import MessageHandler
from message_reader import MessageReader

from message import CollectMessage
from title import CollectTitle

class TestExtractData(unittest.TestCase):

    def setUp(self):
        
        self.message_handler = MessageHandler()
        self.message_reader = MessageReader()
        
        self.server = Server("Testing...", "Testing...", self.message_handler, self.message_reader)
        self.test_client = self.server.app.test_client()

    def test_correct_json_format(self):

        data = {"title": "title", "message": "message"}

        with patch("sqlite3.connect", return_value="not relevant") as connection:
            with patch.object(MessageHandler, "clear_data") as clear:
                with patch.object(MessageHandler, "write_data") as database:   
                        with patch.object(Server, "close_connection") as close:

                            response = self.test_client.post("/send", json=data)
            
                            connection.assert_called_once()
                            close.assert_called_once()
                            clear.assert_called_once()
                            database.assert_called_once()
                            
                            self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                            self.assertEqual(response.status_code, 200)
        
                            result_title = CollectTitle.titles[-1]
                            result_message = CollectMessage.messages[-1]

                            self.assertEqual(result_title.title , "title")
                            self.assertEqual(result_message.message , "message")

                            CollectTitle.clear_titles()
                            CollectMessage.clear_messages()

    def test_less_keys(self):

        data = {"title": "title"}

        with patch("sqlite3.connect", return_value="not relevant") as connection:
            with patch.object(Server, "close_connection") as close:
                with patch.object(MessageHandler, "clear_data") as clear:
                    with patch.object(MessageHandler, "write_data") as write:
            
                        response = self.test_client.post("/send", json=data)
            
                        connection.assert_called_once()
                        close.assert_called_once()
                        clear.assert_called_once()
                        write.assert_not_called()
                
                        self.assertEqual(response.json, {"Error": "Keys not found"})
                        self.assertEqual(response.status_code, 405)
        
                        result_titles = CollectTitle.titles
                        result_messages = CollectMessage.messages

                        self.assertEqual(len(result_titles) , 0)
                        self.assertEqual(len(result_messages) , 0)


    def test_wrong_key(self):

        data = {"title": "title", "letter": "letter"}

        with patch("sqlite3.connect", return_value="not relevant") as connection:
            with patch.object(Server, "close_connection") as close:
                with patch.object(MessageHandler, "clear_data") as clear:
                    with patch.object(MessageHandler, "write_data") as write:
                
                        response = self.test_client.post("/send", json=data)
            
                        connection.assert_called_once()
                        close.assert_called_once()
                        clear.assert_called_once()
                        write.assert_not_called()
                
                        self.assertEqual(response.json, {"Error": "Keys not found"})
                        self.assertEqual(response.status_code, 405)
        
                        result_titles = CollectTitle.titles
                        result_messages = CollectMessage.messages

                        self.assertEqual(len(result_titles) , 0)
                        self.assertEqual(len(result_messages) , 0)

    def test_extra_key(self):

        data = {"title": "title", "message": "message", "extra": "extra"}

        with patch.object(MessageHandler, "clear_data") as clear:
            with patch.object(MessageHandler, "write_data") as write:
                with patch("sqlite3.connect", return_value="not relevant") as connection:
                    with patch.object(Server, "close_connection") as close:

                        response = self.test_client.post("/send", json=data)
            
                        connection.assert_called_once()
                        clear.assert_called_once()
                        close.assert_called_once()
                        write.assert_called_once()
                        
                        self.assertEqual(response.json, {"Success": "Thanks for you request!"})
                        self.assertEqual(response.status_code, 200)
        
                        result_titles = CollectTitle.titles
                        result_messages = CollectMessage.messages

                        self.assertEqual(result_titles[-1].title , "title")
                        self.assertEqual(result_messages[-1].message , "message")

                        CollectTitle.clear_titles()
                        CollectMessage.clear_messages()

if __name__ == "__main__":

    unittest.main()

