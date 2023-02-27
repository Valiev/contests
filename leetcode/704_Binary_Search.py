class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            value = nums[mid]
            if value == target:
                return mid
            if value > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
