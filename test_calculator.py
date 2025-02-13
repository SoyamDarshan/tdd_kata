import unittest

from calculator import add, parse_string_nums


class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert add("") == 0
        assert add("1") == 1
        assert add("1,2") == 3
        assert add("1,2,3,4") == 10

    def test_parse_string_nums(self):
        assert parse_string_nums("") == [0]
        assert parse_string_nums("1") == [1]
        assert parse_string_nums("1,2") == [1, 2]
        assert parse_string_nums("1,2,3,4") == [1, 2, 3, 4]



if __name__ == '__main__':
    unittest.main()
