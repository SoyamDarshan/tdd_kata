def parse_string_nums(nums_string, separator=","):
    if not nums_string:
        return [0]
    nums_string = nums_string.strip().split(separator)
    return list(map(int, nums_string))


def add(nums_string):
    numbers = parse_string_nums(nums_string)
    return sum(numbers)
