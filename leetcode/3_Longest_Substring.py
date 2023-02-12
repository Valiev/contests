class Solution1:
    def lengthOfLongestSubstring(self, elems) -> int:
        length = 0

        for idx, start_elem in enumerate(elems):
            uniq = {start_elem}
            length = max(length, len(uniq))
            for elem in elems[idx + 1:]:
                if elem in uniq:
                    break
                uniq.add(elem)
                length = max(length, len(uniq))

        return length


class Solution2:
    """
    Better memory consumption
    """

    def lengthOfLongestSubstring(self, elems) -> int:
        if elems == '':
            return 0
        length = len(elems)
        max_length = 0
        pos_idx = dict()
        pos = 0
        while pos < length:
            elem = elems[pos]
            if elem in pos_idx:
                pos = pos_idx[elem] + 1
                pos_idx = {}
                continue
            pos_idx[elem] = pos
            max_length = max(max_length, len(pos_idx))
            pos += 1
        return max_length
