class ParentPuzzle:
    def __init__(self) -> None:
        self.all_actions: tuple[str, str, str, str] = 'Wolf', 'Goat', 'Cabbage', 'Nothing'
        self.possible_actions: list[str] = []
        self.action: str = ''
        self.lake_positions: dict[str, bool] = {
            'Farmer':False,
            'Wolf':False,
            'Goat':False,
            'Cabbage':False
        }

    def start_puzzle(self):
        """Child classes with custom behaviours should overwrite this method"""
        while not self.is_puzzle_solved():
            self.get_action()

    def is_puzzle_solved(self) -> bool:
        """Returns True if the Wolf, Goat, and Cabbage are all True"""
        return self.lake_positions['Wolf'] == self.lake_positions['Goat'] == \
            self.lake_positions['Cabbage'] == True

    def get_action(self) -> None:
        """How the object gets its actions should depend on the child class"""
        raise Exception('An instance of the parent class should not be made')

    def display_positions(self) -> None:
        """Prints all objects & what side of the river they are on"""
        for key, value in self.lake_positions.items():
            print(f'{key}:{"Right" if value else "Left"}')

    def generate_possible_actions(self):
        """Generates a list of possible moves from the current lake positions"""
        def __can_move_wolf() -> bool:
            """
            Returns True if the farmer and the wolf are on the same side and
            if the goat is not left on the same side as the cabbage
            """
            return self.lake_positions['Farmer'] is self.lake_positions['Wolf']\
                and self.lake_positions['Goat'] != self.lake_positions['Cabbage']

        def __can_move_goat() -> bool:
            """Returns True if the farmer and the goat are on the same side"""
            return self.lake_positions['Farmer'] is self.lake_positions['Goat']

        def __can_move_cabbage() -> bool:
            """
            Returns True if the farmer and the cabbage are on the same side and
            if the wolf is not left on the same side as the goat
            """
            return self.lake_positions['Farmer'] is self.lake_positions['Cabbage']\
                and self.lake_positions['Wolf'] != self.lake_positions['Goat']

        def __can_move_nothing() -> bool:
            """
            Returns True if the wolf is not left on the same side as the goat and
            if the goat is not left on the same side as the cabbage
            """
            return self.lake_positions['Wolf'] != self.lake_positions['Goat']\
                and self.lake_positions['Goat'] != self.lake_positions['Cabbage']

        #  generate_possible_actions starts here
        self.possible_actions = []
        if __can_move_wolf(): self.possible_actions.append('Wolf')
        if __can_move_goat(): self.possible_actions.append('Goat')
        if __can_move_cabbage(): self.possible_actions.append('Cabbage')
        if __can_move_nothing(): self.possible_actions.append('Nothing')

    def perform_action(self) -> None:
        """
        The Farmer always changes sides when this function runs.
        A second object also changes side if 'self.action' doesn't contain None.
        """
        self.lake_positions['Farmer'] = not self.lake_positions['Farmer']
        if self.action != 'Nothing':
            self.lake_positions[self.action] = not self.lake_positions[self.action]