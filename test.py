import unittest
from src import plus, minus

class TestTashizan(unittest.TestCase):
    """test class of src.py
    """

    def test_tashizan(self):
        """test method for src
        """
        value1 = 2
        value2 = 6
        expected = 8
        actual = plus(value1, value2)
        self.assertEqual(expected, actual)

    def test_hikizan(self):
        """test method for src
        """
        value1 = 3
        value2 = 1
        expected = 2
        actual = minus(value1, value2)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()