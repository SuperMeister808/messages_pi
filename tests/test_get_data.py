
import unittest

from unittest.mock import patch

from server import Server

import sqlite3

class TestGetData(unittest.TestCase):

    def setUp(self):
        
        self.server = Server("Testing...", "Testing...")
        self.test_client = self.server.app.test_client()

    def test_correct_database(self):

        title = "title"
        message = "message"
        
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()

        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS messages(
                            title TEXT,
                            message TEXT)
                       """)
        cursor.execute("""INSERT INTO messages (title, message) VALUES (?, ?)""", (title, message))

        with patch("sqlite3.connect", return_value=conn) as connection:
            with patch.object(Server, "close_connection") as close:

                response = self.test_client.get("/get")

                connection.assert_called_once()
                close.assert_called_once()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json, {"colums": ["title", "message"], "rows": [["title", "message"]]})

    def test_empty_database(self):

        conn = sqlite3.connect(":memory:")

        with patch("sqlite3.connect", return_value=conn) as connection:
            with patch.object(Server, "close_connection") as close:

                response = self.test_client.get("/get")

                connection.assert_called_once()
                close.assert_called_once()
                
                self.assertEqual(response.status_code, 405)
                self.assertEqual(response.json, {"Error": "No table found!"})

if __name__ == "__main__":

    unittest.main()


