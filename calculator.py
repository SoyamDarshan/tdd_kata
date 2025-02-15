import re


def parse_string_nums(nums_string, delimiter=None):
    if not delimiter:
        delimiter = ","
    if not nums_string:
        return [0]
    pattern = r'\n|' + delimiter
    nums_string = [int(num) for num in re.split(pattern, nums_string) if num and int(num) < 1000]
    return nums_string


def get_delimiter_nums_string(nums_string):
    if not nums_string.startswith(r'//'):
        return None, nums_string
    delimiter, numbers = nums_string.split("\n", maxsplit=1)
    delimiter = "".join(list(delimiter)[2:])
    delimiter_list = []
    delimiter_str = ""
    for val in delimiter:
        if val == "[":
            delimiter_str = ""
            continue
        if val == "]":
            delimiter_list.append(delimiter_str)
            continue
        delimiter_str += val
    if delimiter_list:
        delimiter = "|".join(sorted(map(re.escape, delimiter_list), reverse=True, key=lambda x: len(x)))
    if delimiter_str and not delimiter_list:
        delimiter = re.escape(delimiter_str)
    return delimiter, numbers


def verify_numbers(numbers):
    errors = [str(num) for num in numbers if num < 0]
    if errors:
        raise ValueError(f"Negatives not allowed {','.join(errors)}")
    return True


def add(nums_string):
    delimiter, nums_string = get_delimiter_nums_string(nums_string)
    numbers = parse_string_nums(nums_string, delimiter)
    assert verify_numbers(numbers) is True
    return sum(numbers)
