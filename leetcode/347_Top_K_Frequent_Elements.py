import heapq as H
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            counter[i] = 1 + counter.get(i, 0)

        heap = []
        for elem, count in counter.items():
            H.heappush(heap, (count, elem))
            if len(heap) > k:
                H.heappop(heap)
        return [e for (c, e) in heap]

