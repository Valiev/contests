class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        acc = []
        merged = False
        for interval in intervals:

            # before
            if interval[1] < newInterval[0]:
                acc.append(interval)
                continue

            # after
            if interval[0] > newInterval[1]:
                if not merged:
                    acc.append(newInterval)
                    merged = True
                acc.append(interval)
                continue

            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])

        if not merged:
            acc.append(newInterval)
        return acc
