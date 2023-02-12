# Beats 91% by runtime

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # looking for even palindromes
        max_len = len(s)
        palindrome_len = 0
        start, end = 0, 0
        for idx, char in enumerate(s):
            max_wing = min(idx, max_len - idx - 1)
            wing_len = 0
            for offset in range(1, max_wing + 1):
                if s[idx - offset] == s[idx + offset]:
                    wing_len += 1
                    continue
                break
            cur_len = 1 + 2 * wing_len

            if cur_len > palindrome_len:
                palindrome_len = cur_len
                start = idx - wing_len
                end = idx + wing_len

        # looking to odd palindromes
        for idx, char in enumerate(s):
            if idx == max_len - 1:
                break
            next_char = s[idx+1]
            if next_char != char:
                continue

            max_wing = min(idx, max_len - idx - 2)
            wing_len = 0
            for offset in range(1, max_wing + 1):
                if s[idx - offset] == s[idx + 1 + offset]:
                    wing_len += 1
                    continue
                break

            cur_len = 2 + 2 * wing_len

            if cur_len > palindrome_len:
                palindrome_len = cur_len
                start = idx - wing_len
                end = idx + 1 + wing_len

        return s[start:end+1]

