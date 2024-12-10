from helpers import input_filepath, Ok, Error

VECTORS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]


def find_start(lines):
    for y, line in enumerate(lines):
        for x, elem in enumerate(line):
            if elem == '^':
                return (x, y)
    raise Exception('not found')


def next_point(lines, x, y, vector_idx, overrides=[]):
    X_MAX = len(lines[0])
    Y_MAX = len(lines)
    dx, dy = VECTORS[vector_idx]
    next_x, next_y = x + dx, y + dy
    if not ((0 <= next_x < X_MAX) and (0 <= next_y < Y_MAX)):
        return None

    if lines[next_y][next_x] == '#' or (next_x, next_y) in overrides:
        vector_idx = (vector_idx + 1) % 4
        next_x, next_y = x, y

    return next_x, next_y, vector_idx


def route(lines, overrides=[]):
    seen = set()
    x, y = find_start(lines)
    vector_idx = 0
    seen.add((x, y, vector_idx))

    out_of_map = False
    while True:
        point = next_point(lines, x, y, vector_idx, overrides)
        if point is None:
            out_of_map = True
            break
        if point in seen:
            break
        else:
            seen.add(point)
        x, y, vector_idx = point

    steps = len(set((x,y) for (x,y,_) in seen))

    if overrides and out_of_map:
        return Error(steps)

    return Ok(steps)


def puzzle1(input_file):
    with open(input_file) as fp:
        return route(fp.readlines())


def puzzle2(input_file):
    with open(input_file) as fp:
        lines = fp.readlines()
    X_MAX = len(lines[0])
    Y_MAX = len(lines)
    total = 0
    for x in range(X_MAX):
        for y in range(Y_MAX):
            if lines[y][x] != '.':
                continue
            result = route(lines, [(x,y)])
            if result.is_ok():
                total += 1
                print(total)

    return total


if __name__ == "__main__":
    input_file = input_filepath("day06.txt")
    result1 = puzzle1(input_file)
    print(result1)
    result2 = puzzle2(input_file)
    print(result2)
