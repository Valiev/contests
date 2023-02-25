class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = None
        profit = 0
        for price in prices:
            if min_price is None:
                min_price = price
                continue
            if price > min_price:
                profit = max(profit, price - min_price)
            else:
                min_price = price
        return profit
