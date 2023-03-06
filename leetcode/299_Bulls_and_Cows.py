class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        cache = {}
        for (s, g) in zip(secret, guess):
            if s == g:
                bulls += 1
                continue

            cache[s] = cache.get(s, 0) + 1
            if cache[s] <= 0:
                cows += 1
            cache[g] = cache.get(g, 0) - 1
            if cache[g] >= 0:
                cows += 1

        return f"{bulls}A{cows}B"
