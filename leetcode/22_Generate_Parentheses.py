class Solution:
    def generateParenthesis(self, n: int, cache={}) -> List[str]:
        if n in cache:
            return cache[n]

        if n == 1:
            res = ["()"]
            cache[1] = res
            return cache[1]

        # uniq
        acc = set()
        for prev in self.generateParenthesis(n-1):
            acc.add(f"({prev})")

        # combined
        for n_1 in range(1, n//2 + 1):
            m_1 = n - n_1
            for n_pair in self.generateParenthesis(n_1, cache=cache):
                for m_pair in self.generateParenthesis(m_1, cache=cache):
                    acc.add(f"{n_pair}{m_pair}")
                    acc.add(f"{m_pair}{n_pair}")
        cache[n] = list(acc)
        return cache[n]
