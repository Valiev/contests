from helpers import input_filepath, Ok, Error

VALUES = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def check_line(line, functions):
    left, right = line.split(': ')
    desired_value = int(left)
    values = [int(i) for i in right.split()]

    def dfs(cur, pos):
        if cur == desired_value:
            return True
        if cur > desired_value:
            return False
        if pos >= len(values):
            return False
        arg = values[pos]

        return any(
            dfs(func(cur, arg), pos+1)
            for func in functions
        )

    if dfs(0, 0):
        return Ok(desired_value)
    return Error(False)


def puzzle(input_file, functions):
    total = 0
    with open(input_file) as fp:
        for line in fp.readlines():
            result = check_line(line, functions)
            if result.is_ok():
                total += result.value
    return total


# 370631131361420
if __name__ == "__main__":
    input_file = input_filepath("day07.txt")
    functions1 = [
        lambda x, y: x + y,
        lambda x, y: x * y,
    ]
    result1 = puzzle(input_file, functions1)
    print(result1)
    functions2 = [
        lambda x, y: x * y,
        lambda x, y: x + y,
        lambda x, y: int(f"{x}{y}")
    ]
    result2 = puzzle(input_file, functions2)
    print(result2)
