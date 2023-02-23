class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_pos = 0
        for pos, n in enumerate(nums):
            if n == val:
                continue

            if next_pos != pos:
                nums[next_pos] = n

            next_pos += 1
        return next_pos
