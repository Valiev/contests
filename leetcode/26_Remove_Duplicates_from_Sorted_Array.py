class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        prev = nums[0]
        cur_pos = 1
        for pos in range(1, len(nums)):
            cur = nums[pos]
            if cur <= prev:
                continue
            nums[cur_pos] = cur
            prev = cur
            cur_pos += 1

        return cur_pos
