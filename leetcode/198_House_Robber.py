class Solution:
    def rob(self, nums: List[int]) -> int:
        total = len(nums)
        if total == 0:
            return 0
        elif total <= 2:
            return max(nums)
        elif total == 3:
            return max(nums[0] + nums[2], nums[1])
        else:
            pass

        a, b, c = nums[-3] + nums[-1], nums[-2], nums[-1]
        for i in range(len(nums)):
            if i in [0, 1, 2]:
                continue
            idx = len(nums) - 1 - i
            a, b, c = nums[idx] + max(b, c), a, b

        return max(a, b)
