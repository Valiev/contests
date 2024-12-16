from helpers import BasePuzzle
from collections import defaultdict
from itertools import batched


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

    def fs_format1(self, filesystem):
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

    def fs_freespaces(self, filesystem):
        stack = []
        for idx, elem in enumerate(filesystem):
            if elem == '.':
                stack.append(idx)
                continue

            if not stack:
                continue

            yield stack[0], len(stack)
            while stack:
                stack.pop()

        if stack:
            yield stack[0], len(stack)

    def fs_format2(self, filesystem):
        file_sizes = defaultdict(int)
        file_poses = dict()
        max_file_id = None
        for idx, elem in enumerate(filesystem):
            if elem == '.':
                continue
            file_sizes[elem] += 1
            if elem not in file_poses:
                file_poses[elem] = idx
            if max_file_id is None:
                max_file_id = elem
            max_file_id = max(max_file_id, elem)

        for file_id in range(max_file_id, -1, -1):
            file_size = file_sizes[file_id]
            print(f'Formatting {file_id} file with {file_size} len')
            file_pos = file_poses[file_id]
            for free_pos, fs_len in self.fs_freespaces(filesystem):
                if free_pos >= file_pos:
                    break
                if file_size > fs_len:
                    continue
                print(f'- Switching with free_space {fs_len} len')
                for i in range(file_size):
                    filesystem[file_pos+i], filesystem[free_pos+i] = filesystem[free_pos+i], filesystem[file_pos+i]
                break
            else:
                print(f'- No switch for {file_id}')

        return filesystem

    def solve(self, format_function):
        filesystem = self.get_filesystem()
        format_function(filesystem)
        for batch in batched(filesystem, 10):
            print(' '.join(str(i) for i in batch))
        return self.fs_checksum(filesystem)

    def solve1(self):
        return self.solve(self.fs_format1)

    def solve2(self):
        return self.solve(self.fs_format2)


if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.solve1())
    print(puzzle.solve2())
