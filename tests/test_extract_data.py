
import unittest

from server import Server

class TestExtractData(unittest.TestCase):

    def setUp(self):
        
        self.server = Server("Testing...", "Testing...")

        self.test_client = self.server.app.test_client()

    def correct_json_format(self):

        data = {"title": "title", "message": "message"}

        response = self.test_client.post("/send", json=data)

        self.assertEqual(response.json, {"Success": "Thanks for you request!"})
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual()



