def is_sub(sub, text):
    if sub == "":
        return True
    pos = 0
    max_pos = len(text) - 1
    for char in sub:
        match = False
        while pos <= max_pos:
            if char == text[pos]:
                match = True
                pos += 1
                break
            else:
                pos += 1

        if match:
            continue
        return False

    return True


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return is_sub(s, t)
