
import unittest
from unittest.mock import patch

from database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):

        self.d = Database()

    def test_correct_arguments(self):

        t = "titel"
        m = "message"
        
        self.d.add_message(t, m)

        return None
    
if __name__ == "__main__":

    unittest.main()