class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0
        for i in nums:
            acc += i
            yield acc
