from itertools import product


class Board:
    def __init__(self, filename):
        self.lines = open(filename).read().splitlines()
        self.X_MAX = len(self.lines[0]) - 1
        self.Y_MAX = len(self.lines) - 1

    def get(self, x, y):
        return self.lines[y][x]

    def iter_symbols_pos(self, whitelist=None):
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char == '.':
                    continue
                if char.isdigit():
                    continue
                if whitelist is None:
                    yield (x, y)
                    continue
                if char in whitelist:
                    yield (x, y)

    def find_num_pos(self, x, y):
        while x - 1 >= 0 and self.get(x-1, y).isdigit():
            x -= 1
        return (x, y)

    def iter_num_pos(self):
        acc = set()
        for sym_x, sym_y in self.iter_symbols_pos():
            for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
                if (dx, dy) == (0, 0):
                    continue

                x = sym_x + dx
                y = sym_y + dy

                if not (0 <= x <= self.X_MAX):
                    continue
                if not (0 <= y <= self.Y_MAX):
                    continue

                if not self.get(x, y).isdigit():
                    continue

                x, y = self.find_num_pos(x, y)

                if (x, y) in acc:
                    continue

                acc.add((x, y))
                yield (x, y)

    def get_num(self, x, y):
        acc = []
        acc.append(self.get(x, y))
        while x + 1 <= self.X_MAX and self.get(x+1, y).isdigit():
            acc.append(self.get(x+1, y))
            x += 1
        return int(''.join(acc))

    def iter_nums(self):
        for x, y in self.iter_num_pos():
            yield self.get_num(x, y)

    def part1(self):
        return sum(self.iter_nums())

    def part2(self):
        total = 0
        for sym_x, sym_y in self.iter_symbols_pos(whitelist=["*"]):
            acc = set()
            for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
                x = sym_x + dx
                y = sym_y + dy
                if not (0 <= x <= self.X_MAX):
                    continue
                if not (0 <= y <= self.Y_MAX):
                    continue

                if not self.get(x, y).isdigit():
                    continue
                acc.add(self.find_num_pos(x, y))
            if len(acc) != 2:
                continue

            total += self.get_num(*acc.pop()) * self.get_num(*acc.pop())
        return total


# def iter_links(list_of_lines):
#     Y_MAX = len(list_of_lines) - 1
#     X_MAX = len(list_of_lines[0]) - 1
#
#     for y, line in enumerate(list_of_lines):
#         for x, char in enumerate(line):
#             if char.isdigit():
#                 continue
#             if char == '.':
#                 continue
#
#             # special char! hooray, checking neighboors
#             for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
#                 if (dx, dy) == (0, 0):
#                     continue
#                 x1, y1 = x + dx, y + dy
#
#                 if not (0 <= x1 <= X_MAX):
#                     continue
#
#                 if not (0 <= y1 <= Y_MAX):
#                     continue
#
#                 if list_of_lines[y1][x1].isdigit():
#                     yield (x1, y1)
#
#
# def find_pos(list_of_lines, link_x, link_y):
#     x = link_x
#     while x - 1 > 0 and list_of_lines[link_y][x-1].isdigit():
#         x -= 1
#     print('find_pos start', link_x, link_y)
#     print('find_pos end', x, link_y)
#     return x, link_y
#
#
# def read_pos(list_of_lines, start_x, start_y):
#     X_MAX = len(list_of_lines[0]) - 1
#     acc = []
#     x = start_x
#     while True:
#         if x > X_MAX:
#             break
#         if not list_of_lines[start_y][x].isdigit():
#             break
#         acc.append(list_of_lines[start_y][x])
#         x += 1
#     result = int(''.join(acc))
#     print([start_x, start_y], result)
#     return result
#
#
# def part1():
#     lines = open('day03.input').read().splitlines()
#     positions = set()
#
#     for link_x, link_y in iter_links(lines):
#         print(link_x, link_y)
#         positions.add(find_pos(lines, link_x, link_y))
#     total = 0
#     for x, y in positions:
#         total += read_pos(lines, x, y)
#     return total

if __name__ == "__main__":
    board = Board('day03.input')
    print('part1', board.part1())
    print('part2', board.part2())
