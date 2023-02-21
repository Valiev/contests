VALUES = dict(
    I=1,
    IV=4,
    V=5,
    IX=9,
    X=10,
    XL=40,
    L=50,
    XC=90,
    C=100,
    CD=400,
    D=500,
    CM=900,
    M=1000,
)


class Solution:
    def romanToInt(self, s: str) -> int:
        pos = 0
        total = 0
        while True:
            chunk = s[pos:pos+2]
            if not chunk:
                break
            if chunk in VALUES:
                total += VALUES[chunk]
                pos += 2
                continue

            total += VALUES[chunk[0]]
            pos += 1
        return total
