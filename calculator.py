def parse_string_nums(nums_string):
    if not nums_string:
        return [0]
    return nums_string


def add(nums_string):
    numbers = parse_string_nums(nums_string)
    return sum(numbers)
