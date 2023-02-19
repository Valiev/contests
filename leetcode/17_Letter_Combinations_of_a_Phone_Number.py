MAPPING = {
    2: [i for i in "abc"],
    3: [i for i in "def"],
    4: [i for i in "ghi"],
    5: [i for i in "jkl"],
    6: [i for i in "mno"],
    7: [i for i in "pqrs"],
    8: [i for i in "tuv"],
    9: [i for i in "wxyz"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        acc = []
        head = int(digits[0])
        tail = digits[1:]
        if not tail:
            return MAPPING[head]

        for option in MAPPING[head]:
            for combination in self.letterCombinations(tail):
                acc.append(option + combination)
        return acc

