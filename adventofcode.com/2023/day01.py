TXT2DIGIT = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
}


def calibration_from_line1(line):
    digits = list(filter(str.isdigit, line))
    return int(f"{digits[0]}{digits[-1]}")


def calibration_from_line2(line):
    first_pos = len(line)
    last_pos = -1
    first_word, last_word = None, None

    for word in TXT2DIGIT:
        find = line.find(word)
        if find == -1:
            continue
        if find < first_pos:
            first_pos = find
            first_word = word

    for word in TXT2DIGIT:
        rfind = line.rfind(word)
        if rfind == -1:
            continue
        if rfind > last_pos:
            last_pos = rfind
            last_word = word

    return 10 * TXT2DIGIT[first_word] + TXT2DIGIT[last_word]


def calibration_from_file(filename, calibration_line_func):
    total = 0
    for line in open(filename):
        total += calibration_line_func(line)
    return total


if __name__ == "__main__":
    options = {
            "part1": calibration_from_line1,
            "part2": calibration_from_line2
    }
    for option, func in options.items():
        print(option, ":", calibration_from_file('day01.input', func))
