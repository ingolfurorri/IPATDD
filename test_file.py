import unittest
from kata import add 

class AddTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(add(""), "")
    
    def test_single_num(self):
        self.assertEqual(add("1"), 1)
    
    def test_two_num(self):
        self.assertEqual(add("1,2"), 3)