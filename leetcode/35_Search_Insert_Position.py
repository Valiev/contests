class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid
                continue

            if target <= nums[mid]:
                right = mid
                continue

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return right
