def river_puzzle():
    lake_positions = {'Farmer':False,'Wolf':False,'Goat':False,'Cabbage':False}
    while True:
        print()
        display_positions(lake_positions)
        choice = input('Type what to move (or Nothing): ').lower()
        if choice.startswith('w') and can_transport_wolf(lake_positions):
            lake_positions = transport_object(lake_positions, 'Wolf')

        elif choice.startswith('g') and can_transport_goat(lake_positions):
            lake_positions = transport_object(lake_positions, 'Goat')

        elif choice.startswith('c') and can_transport_cabbage(lake_positions):
            lake_positions = transport_object(lake_positions, 'Cabbage')

        elif choice.startswith('n') and can_transport_nothing(lake_positions):
            lake_positions = transport_object(lake_positions, None)

        else: print('Impossible Action')

        if win_condition(lake_positions):
            print('Winner!')
            break


def display_positions(lake_pos) -> None:
    print(f'Farmer:{left_or_right(lake_pos["Farmer"])}')
    print(f'Wolf:{left_or_right(lake_pos["Wolf"])}')
    print(f'Goat:{left_or_right(lake_pos["Goat"])}')
    print(f'Cabbage:{left_or_right(lake_pos["Cabbage"])}')


def left_or_right(item) -> str:
    return 'Right' if item else 'Left'


def can_transport_wolf(lake_pos) -> bool:
    """
    Returns True if the farmer and the wolf are on the same side and
    if the goat is not left on the same side as the cabbage
    """
    return lake_pos['Farmer'] is lake_pos['Wolf'] and \
    lake_pos['Goat'] != lake_pos['Cabbage']


def can_transport_goat(lake_pos) -> bool:
    """
    Returns True if the farmer and the goat are on the same side
    """
    return lake_pos['Farmer'] is lake_pos['Goat']


def can_transport_cabbage(lake_pos) -> bool:
    """
    Returns True if the farmer and the cabbage are on the same side and
    if the wolf is not left on the same side as the goat
    """
    return lake_pos['Farmer'] is lake_pos['Wolf'] and \
    lake_pos['Wolf'] != lake_pos['Goat']


def can_transport_nothing(lake_pos) -> bool:
    """
    Returns True if the wolf is not left on the same side as the goat and
    if the goat is not left on the same side as the cabbage
    """
    return lake_pos['Wolf'] != lake_pos['Goat'] and \
    lake_pos['Goat'] != lake_pos['Cabbage']


def transport_object(lake_pos, obj_to_trans) -> dict:
    """
    The Farmer always changes sides when this function runs.
    A second object also changes side if obj_to_trans doesn't contain None.
    """
    lake_pos['Farmer'] = not lake_pos['Farmer']
    if obj_to_trans:
        lake_pos[obj_to_trans] = not lake_pos[obj_to_trans]
    return lake_pos


def win_condition(lake_pos) -> bool:
    """
    Returns True if the Wolf, Goat, and Cabbage are all True
    """
    return lake_pos['Wolf'] == lake_pos['Goat'] == lake_pos['Cabbage'] == True


if __name__ == '__main__':
    river_puzzle()