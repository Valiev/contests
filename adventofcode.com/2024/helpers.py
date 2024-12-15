from pathlib import Path

INPUT_FOLDER = Path(__file__).parent / "inputs"


def input_filepath(filename):
    return (INPUT_FOLDER / filename).resolve()

class Result:
    def __init__(self, value):
        self.value = value

    def is_ok(self):
        return not self.is_error()

    def is_error(self):
        return not self.is_ok()

    def __str__(self):
        return f"{self.__class__.__name__}({self.value})"

class Ok(Result):
    def is_ok(self):
        return True


class Error(Result):
    def is_error(self):
        return True

class BasePuzzle:
    DAY = '00'

    def __init__(self):
        self.file = input_filepath(f"day{self.DAY}.txt")

    def read_input(self):
        with open(self.file) as fp:
            return fp.read()

    def read_input_lines(self):
        with open(self.file) as fp:
            for line in fp:
                yield line.strip()

    def solve1(self):
        raise NotImplementedError

    def solve2(self):
        raise NotImplementedError


