I = 'I'
V = 'V'
X = 'X'
L = 'L'
C = 'C'
D = 'D'
M = 'M'

# curr, curr5, curr10
POWERS = {
    0: (I, V, X),
    1: (X, L, C),
    2: (C, D, M),
    3: (M, '', '')
}


def power_to_roman(power):
    curr, curr5, curr10 = POWERS[power]
    return {
        0: '',
        1: curr,
        2: curr * 2,
        3: curr * 3,
        4: curr + curr5,
        5: curr5,
        6: curr5 + curr,
        7: curr5 + curr * 2,
        8: curr5 + curr * 3,
        9: curr + curr10
    }


POWER_MAP = {i: power_to_roman(i) for i in POWERS}


class Solution:
    def intToRoman(self, num: int) -> str:
        acc = []
        power = 0
        while num != 0:
            acc.append(POWER_MAP[power][num % 10])
            power += 1
            num //= 10
        return ''.join(acc[::-1])
