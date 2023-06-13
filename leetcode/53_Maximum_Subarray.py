class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = None
        cur = None
        for n in nums:
            if cur is None:
                cur = n
                best = n
                continue
            cur = max(n, cur + n)
            best = max(best, cur)
        return best
