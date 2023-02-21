class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        right_sum = total
        for idx, mid in enumerate(nums):
            right_sum -= mid
            if right_sum == left_sum:
                return idx
            left_sum += mid
        return -1
