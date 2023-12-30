from typing import List


COUNTED = 'X'


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Y_MAX = len(grid) - 1
        X_MAX = len(grid[0]) - 1

        def area(x, y):
            counter = 0
            if grid[y][x] == 1:
                counter += 1
                grid[y][x] = COUNTED
            else:
                return counter

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x1, y1 = x+dx, y+dy
                if not (0 <= x1 <= X_MAX):
                    continue
                if not (0 <= y1 <= Y_MAX):
                    continue

                counter += area(x1, y1)
            return counter

        max_area = 0
        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                if value == 0:
                    continue
                if value == COUNTED:
                    continue

                max_area = max(max_area, area(x, y))
        return max_area
