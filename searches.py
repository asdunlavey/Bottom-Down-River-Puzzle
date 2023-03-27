from parent_puzzle import ParentPuzzle
from time import time


class Searches(ParentPuzzle):
    def __init__(self):
        super().__init__()
        self.pop_type: int = 0
        self.depth_limit: int = 0
        self.starting_time: float = 0
        self.current_sequence: list[str] = []
        self.all_sequences: list[list] = [['Goat']]  # The only valid 1st move
        self.successful_sequences: list[list] = []

    def start_puzzle(self):
        self.get_pop_type()
        self.get_depth()
        self.toggle_timer()
        while self.all_sequences:
            self.reset_puzzle()
            self.get_action()
        self.toggle_timer()
        self.most_efficient_routes()

    def get_pop_type(self):
        """Determines what search method to use, based on the user's choice."""
        search_types: dict[str, int] = {'Breadth':0, 'Depth':-1}
        print(options := tuple(search_types.keys()))
        choice: str = ''
        while choice not in options:
            choice = input('Enter what type of search to use: ')
        self.pop_type = search_types[choice]

    def toggle_timer(self):
        if self.starting_time == 0:
            self.starting_time = time()
        else:
            print(f'Execution time: {time() - self.starting_time} seconds')
            self.starting_time = 0

    def get_depth(self):
        while True:
            self.depth_limit = input('Enter how many layers deep you want to search (1~19): ')
            if self.depth_limit.isdigit():
                self.depth_limit = int(self.depth_limit)
                if 20 > self.depth_limit > 0: return

    def reset_puzzle(self):
        self.lake_positions = {
            'Farmer': False,
            'Wolf': False,
            'Goat': False,
            'Cabbage': False
        }

    def get_action(self):
        self.current_sequence = self.all_sequences.pop(self.pop_type)
        if self.too_deep(): return
        self.perform_sequence()
        print(self.current_sequence)
        self.search_next_layer()

    def perform_sequence(self):
        for self.action in self.current_sequence:
            self.perform_action()

    def search_next_layer(self):
        self.generate_possible_actions()
        for self.action in self.possible_actions:
            self.perform_action()
            if self.is_puzzle_solved():
                #  input(f'{self.current_sequence + [self.action]} {len(self.current_sequence) + 1}')
                self.successful_sequences.append(self.current_sequence + [self.action])
            else:
                self.all_sequences.append(self.current_sequence + [self.action])
            self.perform_action()

    def too_deep(self) -> bool:
        """Has the current sequence reached the depth limit?"""
        return len(self.current_sequence) == self.depth_limit

    def most_efficient_routes(self):
        """Displays the routes that took the fewest actions."""
        if not self.successful_sequences:
            print(f'{self.depth_limit} moves is not enough to solve the puzzle.')
            return
        self.successful_sequences.sort(key=len)
        least_moves = len(self.successful_sequences[0])
        print(f'Solutions with the fewest moves ({least_moves})')
        for index in range(len(self.successful_sequences)):
            if len(self.successful_sequences[index]) > least_moves: break
            else: print(self.successful_sequences[index])
