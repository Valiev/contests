class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n, a, b = len(cost), cost[-2], cost[-1]
        for i in range(2, n):
            pos = n - 1 - i
            a, b = cost[pos] + min(a, b), a
        return min(a, b)
