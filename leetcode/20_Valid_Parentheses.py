OPEN = "[({"
CLOSE = "})]"

def pair(s):
    return {
        '[': ']',
        ']': '[',
        '(': ')',
        ')': '(',
        '{': '}',
        '}': '{',
    }[s]


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in OPEN:
                stack.append(char)
                continue
            # close
            # empty stack
            if not stack:
                return False
            if stack[-1] == pair(char):
                stack.pop()
                continue
            return False

        if stack:
            return False

        return True
