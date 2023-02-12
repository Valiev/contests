# Beats 68% CPU
# Beats 82% MEM


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_valid = len(nums)
        # rearrange
        for pos in range(max_valid):
            while True:
                num = nums[pos]
                if num == pos + 1:
                    break
                if num > max_valid:
                    break
                if num < 1:
                    break
                # swap
                dest_pos = num - 1
                if num == nums[dest_pos]:
                    break
                nums[pos], nums[dest_pos] = nums[dest_pos], num

        # check
        for pos, num in enumerate(nums, start=1):
            if pos == num:
                continue
            return pos
        return max_valid + 1
