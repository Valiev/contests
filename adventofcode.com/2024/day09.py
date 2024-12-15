from helpers import BasePuzzle


class Puzzle(BasePuzzle):
    DAY = '09'

    def get_filesystem(self):
        line = list(self.read_input_lines())[0]
        filesystem = []
        for pos, count in enumerate(line):
            count = int(count)
            is_file = pos % 2 == 0
            if is_file:
                content = pos // 2
            else:
                content = '.'

            for _ in range(count):
                filesystem.append(content)
        return filesystem

    def fs_checksum(self, filesystem):
        checksum = 0
        for idx, elem in enumerate(filesystem):
            if elem == '.':
                continue
            checksum += idx * elem
        return checksum

    def solve1(self):
        filesystem = self.get_filesystem()
        left, right = 0, len(filesystem) - 1
        while left < right:
            L = filesystem[left]
            R = filesystem[right]
            if L != '.':
                left += 1
                continue

            if R == '.':
                right -= 1
                continue

            filesystem[left] = R
            filesystem[right] = L
        return self.fs_checksum(filesystem)


if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.solve1())
