from manual_control import ManualControl
from searches import Searches


def select_object() -> object:
    """Determines what object to create, based on the user's choice."""
    puzzles: dict[str, object] = {
        'Manual':ManualControl(),
        'Searches':Searches()
    }

    print(options := tuple(puzzles.keys()))
    choice: str = ''
    while choice not in options:
        choice = input('Enter what child class to call: ')
    return puzzles[choice]


if __name__ == '__main__':
    puzzle: object = select_object()
    puzzle.start_puzzle()
