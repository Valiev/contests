from helpers import input_filepath, Ok, Error
# from re import findall, Match
import re

DONT = "don't()"
DO = "do()"


def scan_line(line):
    for part in line.split('mul'):
        if ',' not in part:
            yield Error(part)
            continue

        l, r = part.split(',', 1)
        # LEFT
        if not l.startswith('('):
            yield Error(part)
            continue

        l = l[1:]
        if not l.isdigit():
            yield Error(part)
            continue

        if not len(l) <= 3:
            yield Error(part)
            continue

        # RIGHT
        if ')' not in r:
            yield Error(part)
            continue

        r = r.split(')')[0]
        if not r.isdigit():
            yield Error(part)
            continue

        if not len(r) <= 3:
            yield Error(part)
            continue

        # Success
        yield Ok((int(l), int(r)))


def calc_program(filename):
    with open(filename) as fp:
        return calc_program_lines(fp.readlines())


def find_tokens(line):
    return re.findall(
        r"(don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\))",
        line
    )


def calc_mul(string):
    match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', string)
    ints = [int(i) for i in match.groups()]
    return ints[0] * ints[1]


def calc_lines2(lines):
    do_flag = True
    muls = []
    for line in lines:
        for token in find_tokens(line):
            if token == DONT:
                do_flag = False
                continue

            if token == DO:
                do_flag = True
                continue

            if not do_flag:
                continue

            muls.append(token)

    return sum(calc_mul(mul) for mul in muls)


def calc_program_lines(lines):
    total = 0
    for line in lines:
        if not line.strip():
            continue
        for result in scan_line(line):
            if not result.is_ok():
                continue
            total += (result.value[0] * result.value[1])
    return total


def calc_program2(filename):
    with open(filename) as fp:
        return calc_lines2(fp.readlines())


if __name__ == "__main__":
    input_file = input_filepath("day03.txt")
    result = calc_program(input_file)
    result2 = calc_program2(input_file)
    print(result)
    print(result2)
