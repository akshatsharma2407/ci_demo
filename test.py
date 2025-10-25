import unittest
from app import add, sub

class TestMathfunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,4),6)
    
    def test_sub(self):
        self.assertEqual(sub(2,4),-2)

if __name__ == "__main__":
    unittest.main()