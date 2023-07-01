class Solution:
    def hammingWeight(self, n: int) -> int:
        init = 0
        while n != 0:
            init += (1 & n)
            n >>= 1
        return init
