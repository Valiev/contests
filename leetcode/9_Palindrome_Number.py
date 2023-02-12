class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        acc = []
        while True:
            remainder = x % 10
            acc.append(remainder)
            x //= 10
            if x == 0:
                break
        print(acc)
        total = len(acc)
        for i in range(total // 2 + 1):
            if acc[i] != acc[-i-1]:
                return False
        return True

