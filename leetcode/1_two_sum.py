from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        for idx, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in positions:
                return [idx, positions[num2]]
            positions[num1] = idx
        return []
