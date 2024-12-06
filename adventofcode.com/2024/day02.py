from helpers import input_filepath, Ok, Error

MIN_INCREASE = 1
MAX_INCREASE = 3


def safe_report(nums):
    direction = None
    prev = None
    for pos, num in enumerate(nums):
        if prev is None:
            prev = num
            continue

        delta = abs(num - prev)
        if not (MIN_INCREASE <= delta <= MAX_INCREASE):
            return Error(pos)

        if num > prev:
            cur_direction = +1
        else:
            cur_direction = -1

        prev = num

        if direction is None:
            direction = cur_direction
            continue

        if direction != cur_direction:
            return Error(pos)

    return Ok(True)


def count_safe_reports(filename):
    total = 0
    with open(filename) as fp:
        for line in fp:
            if not line.strip():
                continue
            nums = [int(i) for i in line.strip().split()]
            if safe_report(nums).is_ok():
                total += 1
    return total

def count_safe_reports2(filename):
    total = 0
    with open(filename) as fp:
        for line in fp:
            if not line.strip():
                continue

            nums = [int(i) for i in line.strip().split()]
            result = safe_report(nums)
            if result.is_ok():
                total += 1
                continue

            for pos in range(len(nums)):
                value = nums.pop(pos)
                if safe_report(nums).is_ok():
                    total += 1
                    break
                nums.insert(pos, value)

    return total

if __name__ == "__main__":
    input_file = input_filepath("day02.txt")
    print(count_safe_reports(input_file))
    print(count_safe_reports2(input_file))
