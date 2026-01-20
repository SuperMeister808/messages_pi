
import unittest
from unittest.mock import patch

from database import Database

<<<<<<< Updated upstream
class TestDatabase(unittest.TestCase):

    def setUp(self):

        self.d = Database()

    def test_correct_arguments(self):

        t = "titel"
        m = "message"
        
        self.d.add_message(t, m)

        return None
=======
import sqlite3

class TestDatabase(unittest.TestCase):

    def test_correct_arguments(self):

        data = {"titel": "Greet", "message": "Hello World!"}
        
        with sqlite3.connect(":memory:") as conn:
        
            d = Database()

            d.add_message(conn, data["titel"], data["message"])

            cursor = conn.cursor()

            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            self.assertEqual(colums, )  
>>>>>>> Stashed changes
    
if __name__ == "__main__":

    unittest.main()