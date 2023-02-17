class Solution:
    def area(self, left, right, arr):
        if left == right:
            return 0
        next_left = left
        next_right = right
        if arr[left] < arr[right]:
            next_left += 1
        else:
            next_right -= 1

        return max(
            (right - left) * min(arr[left], arr[right]),
            self.area(next_left, next_right, arr)
        )

    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        return self.area(0, n, height)
