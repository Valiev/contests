class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start_flag = True
        shift = 0
        left = 0
        cur_left = 0
        n = len(nums)
        if n == 1:
            return 1

        while True:
            if start_flag:
                shift = 0
                start_flag = False
                cur_left = left
            else:
                shift = max(shift + 2, shift * 2)

            pos = cur_left + shift

            # edges
            if pos >= n:
                start_flag = True
                continue

            if pos == n - 1:
                if nums[pos-1] != nums[pos]:
                    return nums[pos]

            # update left
            if nums[pos] == nums[pos+1]:
                left = pos
                continue

            if nums[pos-1] == nums[pos]:
                start_flag = True
                continue

            return nums[pos]

