class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = {}
        window = {}
        for char in p:
            pattern[char] = 1 + pattern.get(char, 0)
            window[char] = 0

        p_len = len(p)
        s_len = len(s)
        res = []
        if p_len > s_len:
            return res

        for char in s[:p_len]:
            if char not in window:
                continue
            window[char] += 1

        if window == pattern:
            res.append(0)

        for pos in range(s_len):
            if pos + p_len >= s_len:
                break

            # sub `pos`, add `pos + len`
            sub = s[pos]
            add = s[pos+p_len]

            if sub in window:
                window[sub] = max(0, window[sub] - 1)
            if add in window:
                window[add] += 1
            if window == pattern:
                res.append(pos+1)

        return res
