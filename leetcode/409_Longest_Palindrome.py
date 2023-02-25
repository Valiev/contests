class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for char in s:
            counter[char] = 1 + counter.get(char, 0)
        max_even = 0
        length = 0
        for char, value in counter.items():
            if value % 2 == 0:
                length += value
            else:
                max_even = max(max_even, value)
                length += (value - 1)
        if max_even > 0:
            return length + 1
        return length
