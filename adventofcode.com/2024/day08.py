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

def puzzle1(input_file):
    lines = []
    with open(input_file) as fp:
        for line in fp:
            # having '\n' in line changes the final answer
            lines.append(line.strip())


    X_MAX = len(lines[0])
    Y_MAX = len(lines)

    antinodes = set()
    locations = get_locations(lines)

    for _, antinode in antinode_locations(locations):
        if not (0 <= antinode[0] < X_MAX):
            continue
        if not (0 <= antinode[1] < Y_MAX):
            continue
        antinodes.add(antinode)

    return len(antinodes)


if __name__ == "__main__":
    input_file = input_filepath("day08.txt")
    result1 = puzzle1(input_file)
    print(result1)
