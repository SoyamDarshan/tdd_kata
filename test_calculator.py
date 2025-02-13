import unittest

from calculator import add, get_delimiter_nums_string, parse_string_nums, verify_numbers


class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert add("") == 0
        assert add("1") == 1
        assert add("1,2") == 3
        assert add("1,2,3,4") == 10
        assert add("1\n2,3") == 6
        assert add("1\n") == 1
        assert add("1\n,\n2\n") == 3
        assert add("//;\n1;2;3;4") == 10
        with self.assertRaises(ValueError, msg="Negatives not allowed -1"):
            add("-1,2")
        with self.assertRaises(ValueError, msg="Negatives not allowed -2"):
            add("1,-2")
        with self.assertRaises(ValueError, msg="Negatives not allowed -1, -2"):
            add("-1,-2")

    def test_parse_string_nums(self):
        assert parse_string_nums("") == [0]
        assert parse_string_nums("1") == [1]
        assert parse_string_nums("1,2") == [1, 2]
        assert parse_string_nums("1,2,3,4") == [1, 2, 3, 4]
        assert parse_string_nums("1\n2,3") == [1, 2, 3]
        assert parse_string_nums("1\n") == [1]
        assert parse_string_nums("1\n,\n2\n") == [1, 2]
        assert parse_string_nums("1;\n2;\n3", delimiter=";") == [1, 2, 3]
        assert parse_string_nums("-1,2") == [-1, 2]
        assert parse_string_nums("1,-2") == [1, -2]
        assert parse_string_nums("-1,-2") == [-1, -2]

    def test_get_delimiter_nums_string(self):
        assert get_delimiter_nums_string("") == (None, "")
        assert get_delimiter_nums_string("1") == (None, "1")
        assert get_delimiter_nums_string("1,2") == (None, "1,2")
        assert get_delimiter_nums_string("1,2,3,4") == (None, "1,2,3,4")
        assert get_delimiter_nums_string("1\n2,3") == (None, "1\n2,3")
        assert get_delimiter_nums_string("1\n") == (None, "1\n")
        assert get_delimiter_nums_string("1\n,\n2\n") == (None, "1\n,\n2\n")
        assert get_delimiter_nums_string("//;\n1;2;3;4") == (";", "1;2;3;4")
        assert get_delimiter_nums_string("-1,2") == (None, "-1,2")
        assert get_delimiter_nums_string("1,-2") == (None, "1,-2")
        assert get_delimiter_nums_string("-1,-2") == (None, "-1,-2")

    def test_verify_numbers(self):
        assert verify_numbers([0]) is True
        assert verify_numbers([1]) is True
        assert verify_numbers([1, 2]) is True
        assert verify_numbers([1, 2, 3, 4]) is True
        assert verify_numbers([1, 2, 3]) is True
        assert verify_numbers([1]) is True
        assert verify_numbers([1, 2]) is True
        assert verify_numbers([1, 2, 3]) is True
        assert verify_numbers([1, 2, 3]) is True
        with self.assertRaises(ValueError, msg="Negatives not allowed -1"):
            verify_numbers([-1, 2])
        with self.assertRaises(ValueError, msg="Negatives not allowed -2"):
            verify_numbers([1, -2])
        with self.assertRaises(ValueError, msg="Negatives not allowed -1, -2"):
            verify_numbers([-1, -2])


if __name__ == '__main__':
    unittest.main()
