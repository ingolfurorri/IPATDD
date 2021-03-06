import unittest
from kata import Add 

class AddTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(Add(""), "")
    
    def test_single_num(self):
        self.assertEqual(Add("1"), 1)
    
    def test_two_num(self):
        self.assertEqual(Add("1,2"), 3)

    def test_unknown_numbers(self):
        self.assertEqual(Add("10,2,5,22,1,1"), 41)

    def test_split_on_newline(self):
        self.assertEqual(Add("1\n2"), 3)

    def test_ignore_bigger_1000(self):
        self.assertEqual(Add("1001,2"), 2)

    def test_negative_numbers(self):
        self.assertEqual(Add("-1,2"), 2)

    def test_different_delimiters(self):
        self.assertEqual(Add("//%\n1%2%3"), 6)