class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Using binomial
        """
        S = m - 1 + n - 1
        X = min(m, n) - 1
        nom = 1
        den = 1
        for i in range(1, X+1):
            nom *= (S + 1 - i)
            den *= i
        return nom // den

    def uniquePaths2(self, m: int, n: int) -> int:
        """
        Using cache
        """
        grid = {(0, 0): 1}
        for i in range(m):
            for j in range(n):
                if (i, j) in grid:
                    continue
                grid[(i, j)] = grid.get((i, j - 1), 0) + grid.get((i - 1, j), 0)
        return grid[(m-1, n-1)]
