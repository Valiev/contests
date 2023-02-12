from itertools import islice, zip_longest as zipl

# runtime beats only 13%
# BUT
# memory beats 70%


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        acc = []
        for pos in range(numRows):
            # not paired
            period = 2 * numRows - 2
            if period == 0:
                period = None
            if pos == 0 or pos == numRows - 1:
                for char in islice(s, pos, None, period):
                    acc.append(char)
                continue
            # paired
            shift = 2 * (numRows - 1 - pos)
            s1 = islice(s, pos, None, period)
            s2 = islice(s, pos + shift, None, period)
            for pair in zipl(s1, s2):
                for char in pair:
                    if char is None:
                        continue
                    acc.append(char)

        return ''.join(acc)
