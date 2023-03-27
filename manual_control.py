from parent_puzzle import ParentPuzzle


class ManualControl(ParentPuzzle):
    def __init__(self):
        super().__init__()
        print('ManualControl Object Created')

    def get_action(self):
        def __format_action() -> str:
            """
            This class is designed to understand the user's intended action,
            assuming the first letter matches one of the four possible actions.
            """
            if not self.action: return 'Fail'  # Prevents crashes from an empty variable
            if self.action.startswith('w'): return 'Wolf'
            if self.action.startswith('g'): return 'Goat'
            if self.action.startswith('c'): return 'Cabbage'
            if self.action.startswith('n'): return 'Nothing'

        #  get_action() starts here
        self.display_positions()
        self.generate_possible_actions()
        print(f'Possible Actions = {self.possible_actions}')
        self.action = ''
        while self.action not in self.possible_actions:
            self.action = input('Type what to move (or Nothing): ').lower()
            self.action = __format_action()
        self.perform_action()