MAX = 2 ** 31 - 1
MIN = -2 ** 31


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        x *= sign

        res = 0
        while x != 0:
            res = 10 * res + (x % 10)
            x //= 10

        res *= sign
        if MIN <= res <= MAX:
            return res
        return 0
