class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns, zs, ps = {}, {}, {}
        for i in nums:
            if i < 0:
                ns[i] = ns.get(i, 0) + 1
                continue
            if i == 0:
                zs[i] = zs.get(i, 0) + 1
                continue
            if i > 0:
                ps[i] = ps.get(i, 0) + 1
                continue

        res = set()

        # z, z, z
        if zs:
            if zs[0] >= 3:
                res.add((0,0,0))

        # n, z, p
        if zs:
            for p in ps:
                if (-p) not in ns:
                    continue
                res.add((-p, 0, p))

        # n, n, p
        for n1 in ns:
            if ns[n1] > 1:
                if -2 * n1 in ps:
                    res.add((n1, n1, -2 * n1))

            for n2 in ns:
                if n1 == n2:
                    continue
                if -(n1 + n2) in ps:
                    if n1 < n2:
                        res.add((n1, n2, -(n1 + n2)))
                    else:
                        res.add((n2, n1, -(n1 + n2)))

        # n, p, p
        for p1 in ps:
            if ps[p1] > 1:
                if -2 * p1 in ns:
                    res.add((-2 * p1, p1, p1))

            for p2 in ps:
                if p1 == p2:
                    continue
                if -(p1 + p2) in ns:
                    if p1 < p2:
                        res.add((-(p1 + p2), p1, p2))
                    else:
                        res.add((-(p1 + p2), p2, p1))

        return res

