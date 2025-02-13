def parse_string_nums(nums_string):
    if not nums_string:
        return [0]
    nums_string = nums_string.strip()
    return list(map(int, nums_string))


def add(nums_string):
    numbers = parse_string_nums(nums_string)
    return sum(numbers)
