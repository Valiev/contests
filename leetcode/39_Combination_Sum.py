class Solution:
    def rec(self, cands, target, cache):
        if target in cache:
            return cache[target]

        ret = set()
        for cand in cands:
            if cand > target:
                continue
            if cand == target:
                ret.add((cand,))
                continue
            for res in self.rec(cands, target-cand, cache):
                ret.add(tuple(sorted(res + (cand,))))
        cache[target] = ret
        return cache[target]

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = {}
        return self.rec(candidates, target, cache)
