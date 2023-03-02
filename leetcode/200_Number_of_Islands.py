# Beats 98% CPU
# Beats 91% MEM

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Y = len(grid)
        X = len(grid[0])
        counter = 0
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == '0':
                    continue

                counter += 1
                stack = [(y, x)]
                while stack:
                    b, a = stack.pop()
                    if grid[b][a] == '0':
                        continue
                    grid[b][a] = '0'
                    if b >= 1:
                        stack.append((b - 1, a))
                    if b < Y - 1:
                        stack.append((b + 1, a))
                    if a >= 1:
                        stack.append((b, a - 1))
                    if a < X - 1:
                        stack.append((b, a + 1))

        return counter



