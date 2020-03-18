import unittest
from kata import add 

class AddTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(add(""), "")