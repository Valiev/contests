from helpers import input_filepath, Ok, Error

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
        total = 0
        for line in fp:
            if not line.strip():
                continue

            for result in scan_line(line):
                if not result.is_ok():
                    continue
                total += (result.value[0] * result.value[1]);
    return total


if __name__ == "__main__":
    input_file = input_filepath("day03.txt")
    result = calc_program(input_file)
    print(result)
