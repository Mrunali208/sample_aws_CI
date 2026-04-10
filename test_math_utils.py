import unittest
from math_utils import add

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 6)  # ❌ intentional bug

if __name__ == "__main__":
    unittest.main()
