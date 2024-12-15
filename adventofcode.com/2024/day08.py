from itertools import combinations
from collections import defaultdict
from pprint import pprint
from helpers import BasePuzzle, input_filepath


class Pos:
    def __init__(self, x, y, elem):
        self.x = x
        self.y = y
        self.elem = elem

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y, self.elem)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y, self.elem)

    def __str__(self):
        return f"{self.elem}[{self.x},{self.y}]"

    __repr__ = __str__

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def bounded(self, x_max, y_max):
        return (0 <= self.x < x_max) and (0 <= self.y < y_max)


class Puzzle(BasePuzzle):
    DAY = '08'

    def get_node_locations(self, lines):
        locations = defaultdict(set)
        for y, line in enumerate(lines):
            for x, elem in enumerate(line):
                if elem == '.':
                    continue
                locations[elem].add((x, y))

        return locations

    def get_antinode_locations(self, locations, x_max, y_max, one_time=True):
        for elem in locations:
            for pos1, pos2 in combinations(locations[elem], 2):
                # src = Pos(pos1[0], pos1[1], elem)
                src = Pos(*pos1, elem)
                dst = Pos(*pos2, elem)
                delta = dst - src
                dst_next = dst
                while dst_next.bounded(x_max, y_max):
                    yield dst_next
                    if one_time:
                        break
                    dst_next += delta

                src_next = src
                while src_next.bounded(x_max, y_max):
                    yield src_next
                    if one_time:
                        break
                    src_next -= delta

    def solve(self, one_time):
        lines = list(self.read_input_lines())

        X_MAX = len(lines[0])
        Y_MAX = len(lines)

        locations = self.get_node_locations(lines)
        return len(
            set(
                self.get_antinode_locations(
                    locations, X_MAX, Y_MAX, one_time=one_time
                )
            )
        )

    def solve1(self):
        return self.solve(one_time=True)

    def solve2(self):
        return self.solve(one_time=False)


if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.solve1())
    print(puzzle.solve2())
    # result2 = puzzle2(input_file)
    # # 1047
    # print(result2)
