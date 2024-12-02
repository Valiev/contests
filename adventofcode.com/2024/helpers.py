from pathlib import Path

INPUT_FOLDER = Path(__file__).parent / "inputs"


def input_filepath(filename):
    return (INPUT_FOLDER / filename).resolve()

