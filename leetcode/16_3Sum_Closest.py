from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        mid, right = 0, 0
        closest_sum = None
        for left in range(len(nums)-2):
            mid, right = left+1, len(nums)-1
            if closest_sum is None:
                closest_sum = sum(sorted_nums[i] for i in (left, mid, right))

            remainder = target - sorted_nums[left]
            while mid < right:
                cur_sum = sum(sorted_nums[i] for i in (left, mid, right))
                if cur_sum == target:
                    return cur_sum

                if abs(target - cur_sum) < abs(target - closest_sum):
                    closest_sum = cur_sum

                if remainder > sorted_nums[mid] + sorted_nums[right]:
                    mid += 1
                else:
                    right -= 1
        return closest_sum


s = Solution()
res = s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
print(res)
