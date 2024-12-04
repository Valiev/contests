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

class Ok(Result):
    def is_ok(self):
        return True


class Error(Result):
    def is_error(self):
        return True
