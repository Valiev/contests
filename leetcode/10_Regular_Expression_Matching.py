from itertools import repeat, zip_longest

MAX_LEN = 20


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.dynamic_len = '*' in pattern
        self.wildcard = '.' in pattern

    def __str__(self):
        return f'P[{self.pattern}]'

    __repr__ = __str__

    def get_lens(self):
        if self.dynamic_len:
            return range(MAX_LEN+1)
        return iter([len(self.pattern)])

    def match_len(self, string, length):
        iterable = iter(self.pattern)
        if self.dynamic_len:
            iterable = repeat(self.pattern[0], length)
        for pair in zip_longest(iterable, string[:length]):
            if pair[1] is None:
                return False
            p, c = pair
            if p == '.':
                continue
            if p != c:
                return False
        return True


class Solution:
    def patterns(self, ps):
        if not ps:
            return []

        if '*' in ps:
            l, star, r = ps.partition('*')
            return (
                    self.patterns(l[:-1]) +
                    [Pattern(l[-1] + star)] +
                    self.patterns(r)
            )

        if '.' in ps:
            l, dot, r = ps.partition('.')
            return (
                    self.patterns(l) +
                    [Pattern(dot)] +
                    self.patterns(r)
            )

        return [Pattern(ps)]

    def match(self, string, patterns, cache, s_off, p_off):
        pair = (s_off, p_off)
        if pair in cache:
            return cache[pair]

        s = string[s_off:]
        ps = patterns[p_off:]
        if not ps:
            if s:
                cache[pair] = False
                return False
            cache[pair] = True
            return True

        p = ps[0]
        for p_len in p.get_lens():
            if p_len > len(s):
                continue
            match1 = p.match_len(s, p_len)
            if not match1:
                continue
            match2 = self.match(string, patterns, cache, s_off+p_len, p_off+1)
            if match2:
                cache[pair] = True
                return True

        cache[pair] = False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        patterns = self.patterns(p)
        cache = {}

        result = self.match(s, patterns, cache, 0, 0)
        return result


s = Solution()
tests = {
        ("aa", "a."): True,
        ('a', '.*..a*'): False,
        ("aa", "a*"): True,
        ("aaa", "a."): False,
        ("aa", "a*"): True,
        ("aaa", "a*"): True,
        ("aaaaaaaaaaa", "a*b*"): True,
        ("aaa", ".a*"): True,
        ("aba", ".*a*"): True,
        ("aab", "a*"): False,
        ("aa", "a.*"): True,
        ("ab", "a.*"): True,
        ('aaaaaaaaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*'): False,
        ('aaaaaaaaaaaaaaaaaaa', 'a*a*a*a*a*a*a*a*a*a*'): True,
}

for values, check in tests.items():
    print('Checking', values)
    assert s.isMatch(*values) == check
