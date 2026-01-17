
import unittest
from unittest.mock import patch

from database import Database

class TestDatabase():

    def __init__(self):

        self.d = Database()

    def test_correct_arguments(self):

        t = "Test"
        m = "Das ist ein Test"
        
        self.d.create_table()
        self.d.add_message(t, m)

        return print(self.d.print_table())
    
if __name__ == "__main__":

    test = TestDatabase()
    test.test_correct_arguments()