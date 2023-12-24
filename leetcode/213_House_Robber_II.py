from typing import List


class Solution:
    def rob_index(self, nums, start, end):
        if end - start <= 1:
            return max(nums[i] for i in range(start, end + 1))
        if end - start == 2:
            return max(nums[start] + nums[start + 2], nums[start + 1])

        a, b, c = nums[end-2] + nums[end], nums[end-1], nums[end]
        for i in range(start, end - start + 1):
            if i in [0, 1, 2]:
                continue
            idx = end - i
            a, b, c = nums[idx] + max(b, c), a, b
        return max(a, b)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(
            self.rob_index(nums, 0, len(nums) - 2),
            self.rob_index(nums, 1, len(nums) - 1)
        )
