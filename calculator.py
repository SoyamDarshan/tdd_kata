import re


def parse_string_nums(nums_string, separator=","):
    if not nums_string:
        return [0]
    pattern = r'\n|' + separator
    nums_string = [num for num in re.split(pattern, nums_string) if num]
    return list(map(int, nums_string))


def add(nums_string):
    numbers = parse_string_nums(nums_string)
    return sum(numbers)
