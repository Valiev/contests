class Card:
    def __init__(self, winners, numbers):
        self.winners = set(winners)
        self.numbers = set(numbers)

    @staticmethod
    def from_line(line):
        _, postfix = line.split(': ')
        win_str, num_str = postfix.split(' | ')
        return Card(
            [int(i) for i in win_str.strip().split()],
            [int(i) for i in num_str.strip().split()]
        )

    def winning_numbers(self):
        return len(self.winners & self.numbers)


def part1():
    total = 0
    for line in open('day04.input'):
        card = Card.from_line(line)
        total += int(2 ** (card.winning_numbers() - 1))
    return total


def part2():
    lines = open('day04.input').read().splitlines()
    max_num = len(lines) - 1
    counter = {i: 1 for i in range(len(lines))}
    for idx, line in enumerate(lines):
        mult = counter[idx]
        card = Card.from_line(line)
        updates = [idx + i + 1 for i in range(card.winning_numbers())]
        updates = [i for i in updates if i <= max_num]
        for update in updates:
            counter[update] += mult
    return sum(i for i in counter.values())


if __name__ == "__main__":
    print('part1:', part1())
    print('part2:', part2())
