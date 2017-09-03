import unittest
from src import plus

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

if __name__ == "__main__":
    unittest.main()