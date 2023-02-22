class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for char_s, char_t in zip(s, t):
            match_s = char_s in s_to_t
            match_t = char_t in t_to_s
            if match_s ^ match_t:
                return False

            # match
            if match_s:
                if char_s != t_to_s[char_t]:
                    return False
                if char_t != s_to_t[char_s]:
                    return False
                continue

            # no match
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        return True
