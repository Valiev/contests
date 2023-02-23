class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        for h_pos in range(1 + h_len - n_len):
            for n_pos in range(n_len):
                if needle[n_pos] == haystack[h_pos + n_pos]:
                    continue
                break
            else:
                return h_pos
        return -1
