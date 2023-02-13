def main():
    lake_positions = {'Farmer':False,'Wolf':False,'Goat':False,'Cabbage':False}
    while True:
        display_positions(lake_positions)
        choice = input('Type what to move (or Nothing): ').lower()

        if choice.startswith('w') and can_transport_wolf_successfully(
                lake_positions):
            lake_positions['Farmer'] = not lake_positions['Farmer']
            lake_positions['Wolf'] = not lake_positions['Wolf']

        elif choice.startswith('g') and can_transport_goat_successfully(
                lake_positions):
            lake_positions['Farmer'] = not lake_positions['Farmer']
            lake_positions['Goat'] = not lake_positions['Goat']

        elif choice.startswith('c') and can_transport_cabbage_successfully(
                lake_positions):
            lake_positions['Farmer'] = not lake_positions['Farmer']
            lake_positions['Cabbage'] = not lake_positions['Cabbage']

        elif choice.startswith('n') and can_transport_nothing_successfully(
                lake_positions):
            lake_positions['Farmer'] = not lake_positions['Farmer']

        else: print('Impossible Action')

        if win_condition(lake_positions):
            print('Winner!')
            break
        print()


def display_positions(lake_pos):
    print(f'Farmer:{lake_pos["Farmer"]}')
    print(f'Wolf:{lake_pos["Wolf"]}')
    print(f'Goat:{lake_pos["Goat"]}')
    print(f'Cabbage:{lake_pos["Cabbage"]}')


def can_transport_wolf_successfully(lake_pos):
    """
    Returns True if the farmer and the wolf are on the same side and
    if the goat is not left on the same side as the cabbage
    """
    return lake_pos['Farmer'] is lake_pos['Wolf'] and \
    lake_pos['Goat'] != lake_pos['Cabbage']


def can_transport_goat_successfully(lake_pos):
    """
    Returns True if the farmer and the goat are on the same side
    """
    return lake_pos['Farmer'] is lake_pos['Goat'] # True if on the same side


def can_transport_cabbage_successfully(lake_pos):
    """
    Returns True if the farmer and the cabbage are on the same side and
    if the wolf is not left on the same side as the goat
    """
    return lake_pos['Farmer'] is lake_pos['Wolf'] and \
    lake_pos['Wolf'] != lake_pos['Goat']


def can_transport_nothing_successfully(lake_pos):
    """
    Returns True if the wolf is not left on the same side as the goat and
    if the goat is not left on the same side as the cabbage
    """
    return lake_pos['Wolf'] != lake_pos['Goat'] and \
    lake_pos['Goat'] != lake_pos['Cabbage']


def win_condition(lake_pos):
    return lake_pos['Wolf'] == lake_pos['Goat'] == lake_pos['Cabbage'] == True


if __name__ == '__main__':
    main()