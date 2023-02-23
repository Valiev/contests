def find_peak(nums):
    left, right = 0, len(nums) - 1
    if nums[right] >= nums[left]:
        return right
    while right > left:
        m = (right + left) // 2
        if nums[m] >= nums[left]:
            left = m
        else:
            right = m
        if right - left == 1:
            if nums[right] > nums[left]:
                return right
            return left
    return left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1

        n = len(nums)
        start, end = 0, n-1
        if nums[start] > nums[end]:
            peak = find_peak(nums)
            if target < nums[start]:
                start = peak + 1
            else:
                end = peak

        if target < nums[start]:
            return -1
        if target > nums[end]:
            return -1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid

            if end - start == 1:
                if nums[start] == target:
                    return start
                if nums[end] == target:
                    return end
                return -1
        return start
