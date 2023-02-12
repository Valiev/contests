from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        if total % 2 == 0:
            positions = {total // 2, total // 2 - 1}
        else:
            positions = {(total - 1) // 2}
        to_sum = []
        print(positions)
        for idx, elem in enumerate(self.imerge(nums1, nums2)):
            if not positions:
                continue
            if idx not in positions:
                continue
            to_sum.append(elem)
            positions.remove(idx)
        return float(sum(to_sum)) / len(to_sum)

    def imerge(self, nums1, nums2):
        pos1 = 0
        pos2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        while pos1 < len1 or pos2 < len2:
            if pos1 == len1:
                yield nums2[pos2]
                pos2 += 1
                continue
            if pos2 == len2:
                yield nums1[pos1]
                pos1 += 1
                continue
            elem1 = nums1[pos1]
            elem2 = nums2[pos2]
            if elem1 < elem2:
                yield elem1
                pos1 += 1
                continue
            else:
                yield elem2
                pos2 += 1
                continue
