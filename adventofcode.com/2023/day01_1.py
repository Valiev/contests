def calibration_from_line(line):
    digits = list(filter(str.isdigit, line))
    return int(f"{digits[0]}{digits[-1]}")


def calibration_from_file(filename):
    total = 0
    for line in open(filename):
        total += calibration_from_line(line)
    return total


if __name__ == "__main__":
    result = calibration_from_file('day01.txt')
    print(result)
