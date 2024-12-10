from helpers import input_filepath, Ok, Error


def check_line(line):
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
        return dfs(cur * values[pos], pos+1) or dfs(cur + values[pos], pos+1)

    if dfs(0, 0):
        return Ok(desired_value)
    return Error(False)


def puzzle1(input_file):
    total = 0
    with open(input_file) as fp:
        for line in fp.readlines():
            result = check_line(line)
            if result.is_ok():
                total += result.value
    return total


if __name__ == "__main__":
    input_file = input_filepath("day07.txt")
    result1 = puzzle1(input_file)
    print(result1)
