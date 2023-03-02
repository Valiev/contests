class Solution:
    def climbStairs(self, n: int) -> int:
        # F(n) = F(n-1) (1-step) + F(n-2) (2-step)
        a, b = 1, 2
        for _ in range(n-1):
            a, b = b, a + b
        return a
