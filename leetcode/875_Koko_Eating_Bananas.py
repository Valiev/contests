from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_velocity(k):
            return sum((i + k - 1) // k for i in piles) <= h

        # calc bounds
        left, right = 1, 2
        while not check_velocity(right):
            left = right
            right *= 2

        velocity = right
        while left < right:
            mid = (left + right) // 2
            print(left, mid, right)
            if check_velocity(mid):
                velocity = mid
                right = mid - 1
            else:
                left = mid + 1

        if check_velocity(left):
            return left
        else:
            return velocity
