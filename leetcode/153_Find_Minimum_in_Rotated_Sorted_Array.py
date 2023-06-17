class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while right - left > 1:
            mid = left + (right - left) // 2
            print(left, mid, right)
            L = nums[left]
            R = nums[right]
            M = nums[mid]
            # up up
            if L < R:
                return L
            # up down
            if L < M and M > R:
                left = mid
                continue
            # down up
            if L > M and M < R:
                right = mid
                continue

        return min(nums[left], nums[right])
