from helpers import input_filepath

DATA = """\
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""

DATA2 = """\
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""


def count_x_mas(lines):
    counter = 0
    X_MAX = len(lines[0])
    Y_MAX = len(lines)
    for x in range(X_MAX):
        if (x - 1) < 0:
            continue
        if (x + 1) >= X_MAX:
            continue

        for y in range(Y_MAX):
            if (y - 1) < 0:
                continue
            if (y + 1) >= Y_MAX:
                continue

            if lines[y][x] != 'A':
                continue
            chars = set([lines[y+1][x+1], lines[y-1][x-1]])
            if chars != {'M', 'S'}:
                continue
            chars = set([lines[y-1][x+1], lines[y+1][x-1]])
            if chars != {'M', 'S'}:
                continue
            counter += 1
    return counter


def count_xmas_line_simple(line):
    XMAS = 'XMAS'
    counter = 0
    pos = 0
    while True:
        try:
            index = line.index(XMAS, pos)
            counter += 1
            pos = index + 1
        except ValueError:
            return counter
    return counter


def count_xmas_line_dfs(line):
    XMAS = 'XMAS'

    def dfs(xmas_pos, line_pos):
        if xmas_pos == len(XMAS):
            return 1
        if line_pos >= len(line):
            return 0
        xmas_char = XMAS[xmas_pos]
        line_char = line[line_pos]
        result = 0

        if xmas_char == line_char:
            result += dfs(xmas_pos + 1, line_pos + 1)
        result += dfs(xmas_pos, line_pos + 1)
        return result

    result = dfs(0, 0)
    print(line, result)
    return result


def lines_hor(lines):
    for line in lines:
        yield line


def lines_ver(lines):
    X_MAX = len(lines[0])
    Y_MAX = len(lines)
    for x in range(X_MAX):
        yield ''.join(
            lines[i][x]
            for i in range(Y_MAX)
        )


def lines_diag_up(lines):
    X_MAX = len(lines[0])
    Y_MAX = len(lines)
    for d in range(X_MAX + Y_MAX):
        x = 0
        y = d
        while y >= Y_MAX:
            y -= 1
            x += 1
        if x >= X_MAX:
            break
        diag = []
        while x < X_MAX and y >= 0:
            diag.append(lines[y][x])
            x += 1
            y -= 1
        yield ''.join(diag)


def lines_diag_down(lines):
    X_MAX = len(lines[0])
    Y_MAX = len(lines)
    for d in range(X_MAX + Y_MAX):
        x = 0
        y = Y_MAX - 1 - d
        while y < 0:
            y += 1
            x += 1
        if x >= X_MAX:
            break
        diag = []
        while x < X_MAX and y < Y_MAX:
            diag.append(lines[y][x])
            x += 1
            y += 1
        yield ''.join(diag)


def calc_xmas_02(filepath):
    lines = open(filepath).readlines()
    return count_x_mas(lines)


def calc_xmas_01(filepath):
    lines = open(filepath).readlines()
    methods = [
        lines_hor,
        lines_ver,
        lines_diag_up,
        lines_diag_down,
    ]
    total = 0
    for method in methods:
        method_total = 0
        for line in method(lines):
            method_total += count_xmas_line_simple(line)
            method_total += count_xmas_line_simple(line[::-1])
        total += method_total
    return total


if __name__ == "__main__":
    input_file = input_filepath("day04.txt")
    result01 = calc_xmas_01(input_file)
    print(result01)
    result02 = calc_xmas_02(input_file)
    print(result02)

