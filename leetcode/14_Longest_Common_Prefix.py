class Solution:
    def common_iter(self, strs):
        print(list(zip(*strs)))
        for zipped in zip(*strs):
            if len(set(zipped)) == 1:
                yield zipped[0]
            else:
                return

    def longestCommonPrefix(self, strs: List[str]) -> str:
        return "".join(self.common_iter(strs))
