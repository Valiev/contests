from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if not coins:
            return -1
        INF = float('inf')
        cache = [0] + [INF] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    cache[i] = min(cache[i], 1 + cache[i - coin])

        if cache[-1] == INF:
            return -1
        return cache[-1]
