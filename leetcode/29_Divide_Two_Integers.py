MAX = 2 ** 31 - 1
MIN = -2 ** 31


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if divisor == 1:
            if dividend > 0:
                return min(MAX, dividend)
            return max(MIN, dividend)

        sign = 1
        if dividend < 0:
            sign *= (-1)
            dividend *= (-1)
        if divisor < 0:
            sign *= (-1)
            divisor *= (-1)
        if dividend < divisor:
            return 0

        power = 0
        while 2 ** (power + 1) * divisor < dividend:
            power += 1

        max_2 = 2 ** power * divisor
        ret = sign * (2 ** power + self.divide(dividend - max_2, divisor))
        if ret > 0:
            return min(MAX, ret)
        if ret < 0:
            return max(MIN, ret)
        return ret




