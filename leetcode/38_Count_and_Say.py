class Solution:
    CACHE = {1: "1"}
    def countAndSay(self, n: int) -> str:
        if n in self.CACHE:
            return self.CACHE[n]
        prev = self.countAndSay(n-1)
        acc = []
        counter = 0
        last = None
        for char in prev:
            if last is None:
                last = char
                counter = 1
                continue

            if char == last:
                counter += 1
                continue

            acc.append(f"{counter}{last}")
            counter = 1
            last = char
        if counter > 0:
            acc.append(f"{counter}{last}")
        self.CACHE[n] = "".join(acc)
        return self.CACHE[n]
