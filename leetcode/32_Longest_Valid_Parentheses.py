class Solution:
    def longestValidParentheses(self, text: str) -> int:
        stack = []
        positions = [None for _ in range(len(text))]

        for pos, cur_char in enumerate(text):
            if cur_char == ')':
                if not stack:
                    continue
                prev_char, prev_pos = stack.pop()
                if prev_char == '(':
                    positions[prev_pos] = 0
                    positions[pos] = 0
                else:
                    stack = []
            else:
                stack.append((cur_char, pos))

        cur_len = 0
        max_len = 0
        for elem in positions:
            if elem == 0:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
        return max_len
