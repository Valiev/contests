from itertools import combinations
from helpers import input_filepath


def get_locations(lines):
    locations = dict()
    for y, line in enumerate(lines):
        for x, elem in enumerate(line):
            if elem == '.':
                continue
            locations[elem] = locations.get(elem, set())
            locations[elem].add((x, y))
    return locations


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def bounded(self, x_max, y_max):
        return (0 <= self.x < x_max) and (0 <= self.y < y_max)


def antinode_locations(locations):
    for elem in locations:
        for pos1, pos2 in combinations(locations[elem], 2):

            yield (elem, (
                2 * pos2[0] - pos1[0],
                2 * pos2[1] - pos1[1]
            ))
            yield (elem, (
                2 * pos1[0] - pos2[0],
                2 * pos1[1] - pos2[1]
            ))


def antinode_locations2(locations, x_max, y_max):
    for elem in locations:
        for pos1, pos2 in combinations(locations[elem], 2):
            p1 = Pos(*pos1)
            p2 = Pos(*pos2)
            delta = p2 - p1
            p2_antinode = p2 + delta
            while p2_antinode.bounded(x_max, y_max):
                yield p2_antinode
                p2_antinode += p2

            p1_antinode = p1 - delta
            while p1_antinode.bounded(x_max, y_max):
                yield p1_antinode
                p1_antinode += p1


def puzzle1(input_file):
    lines = []
    with open(input_file) as fp:
        for line in fp:
            # having '\n' in line changes the final answer
            lines.append(line.strip())

    X_MAX = len(lines[0])
    Y_MAX = len(lines)

    locations = get_locations(lines)
    antinodes = set()
    for _, antinode in antinode_locations(locations):
        if not (0 <= antinode[0] < X_MAX):
            continue
        if not (0 <= antinode[1] < Y_MAX):
            continue
        antinodes.add(antinode)

    return len(antinodes)

def puzzle2(input_file):
    lines = []
    with open(input_file) as fp:
        for line in fp:
            # having '\n' in line changes the final answer
            lines.append(line.strip())

    X_MAX = len(lines[0])
    Y_MAX = len(lines)

    antinodes = set()
    locations = get_locations(lines)
    for antinode in antinode_locations2(locations, X_MAX, Y_MAX):
        antinodes.add(antinode)
    return len(antinodes)



if __name__ == "__main__":
    input_file = input_filepath("day08.txt")
    result1 = puzzle1(input_file)
    print(result1)
    result2 = puzzle2(input_file)
    print(result2)
