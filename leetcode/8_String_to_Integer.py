DIGITS = {str(i): i for i in range(10)}
MAX = 2 ** 31 - 1
MIN = -(2 ** 31)


class Solution:
    def filter(self, s):
        whitespace = ' '
        begining = True
        sign_flag = False
        for char in s:
            if char == whitespace:
                if begining:
                    continue
                else:
                    return
            begining = False
            if char in ['+', '-']:
                if not sign_flag:
                    sign_flag = True
                    yield char
                    continue
                return
            sign_flag = True

            if char in DIGITS:
                yield DIGITS[char]
                continue

            return

    def myAtoi(self, s: str) -> int:
        first = True
        acc = 0
        sign = +1
        for elem in self.filter(s):
            if first:
                first = False
                if elem == '-':
                    sign *= (-1)
                    continue
                if elem == '+':
                    continue

            acc = acc * 10 + elem

        if sign > 0:
            acc = min(MAX, acc)
        else:
            acc = max(MIN, sign * acc)
        return acc
