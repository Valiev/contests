class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        row = 0
        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif up == down:
                return False
            if matrix[mid][0] > target:
                down = mid - 1
                continue
            if matrix[mid][-1] < target:
                row = mid
                up = mid + 1
                continue

        print(row)
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            if left == right:
                return matrix[row][left] == target

            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
