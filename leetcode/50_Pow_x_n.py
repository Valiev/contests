class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1.0 / x
            n *= (-1)

        res = x
        pwr = 1
        while 2 * pwr <= n:
            res *= res
            pwr *= 2
        return res * self.myPow(x, n - pwr)
