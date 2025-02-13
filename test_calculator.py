import unittest

from calculator import add, parse_string_nums


class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert add("") == 0
        assert add("1") == 1

    def test_parse_string_nums(self):
        assert parse_string_nums("") == [0]
        assert parse_string_nums("1") == [1]


if __name__ == '__main__':
    unittest.main()
