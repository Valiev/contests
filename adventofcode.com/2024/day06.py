from helpers import input_filepath

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


def next_point(lines, x, y, vector_idx):
    X_MAX = len(lines[0])
    Y_MAX = len(lines)
    dx, dy = VECTORS[vector_idx]
    next_x, next_y = x + dx, y + dy
    if not ((0 <= next_x < X_MAX) and (0 <= next_y < Y_MAX)):
        return None

    if lines[next_y][next_x] == '#':
        vector_idx = (vector_idx + 1) % 4
        next_x, next_y = x, y

    return next_x, next_y, vector_idx


def route(lines):
    seen = set()
    x, y = find_start(lines)
    vector_idx = 0
    seen.add((x, y, vector_idx))

    while True:
        point = next_point(lines, x, y, vector_idx)
        if point is None:
            break
        if point in seen:
            break
        else:
            seen.add(point)
        x, y, vector_idx = point

    return len(set((x,y) for (x,y,_) in seen))


def puzzle1(input_file):
    with open(input_file) as fp:
        return route(fp.readlines())


if __name__ == "__main__":
    input_file = input_filepath("day06.txt")
    result1 = puzzle1(input_file)
    print(result1)

