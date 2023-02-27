# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while right != left:
            mid = (right + left) // 2
            print(left, right)
            flag = isBadVersion(mid)
            if flag:
                right = mid
            else:
                left = mid + 1
        return right
