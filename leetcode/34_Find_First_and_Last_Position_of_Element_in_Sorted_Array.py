NOT_FOUND = [-1, -1]
class Solution:
    def find_border(self, nums, pos, is_right=True):
        target = nums[pos]
        border = 0
        if is_right:
            border = len(nums) - 1

        while border != pos:
            mid = (pos + border) // 2
            if nums[mid] != target:
                border = mid
            else:
                pos = mid
            if abs(border - pos) == 1:
                if nums[border] == target:
                    return border
                else:
                    return pos
        return pos

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        if nums == []:
            return NOT_FOUND

        if left == right:
            if nums[left] == target:
                return [left, right]
            else:
                return NOT_FOUND

        pos = None
        while left != right:
            mid = (left + right) // 2
            value = nums[mid]
            if value > target:
                right = mid
            if value < target:
                left = mid
            if value == target:
                pos = mid
                break

            if right - left <= 1:
                if nums[right] == target:
                    pos = right

                if nums[left] == target:
                    pos = left

                break

        if pos is None:
            return NOT_FOUND

        left = self.find_border(nums, pos, is_right=False)
        right = self.find_border(nums, pos, is_right=True)
        return [left, right]
