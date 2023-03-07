def reverse_letters(text: str):
    n = len(text)
    backs = 0
    for i in range(n):
        pos = n - 1 - i
        char = text[pos]

        if char == '#':
            backs += 1
            continue

        if backs > 0:
            backs -= 1
            continue

        yield char


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        iter_s = reverse_letters(s)
        iter_t = reverse_letters(t)
        while True:
            try:
                char_s = next(iter_s)
            except StopIteration:
                char_s = None
            try:
                char_t = next(iter_t)
            except StopIteration:
                char_t = None
            if char_s != char_t:
                return False
            if char_s is None:
                break
        return True

