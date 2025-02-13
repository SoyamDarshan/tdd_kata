import unittest

from calculator import add


class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert add("") == 0  # add assertion here


if __name__ == '__main__':
    unittest.main()
