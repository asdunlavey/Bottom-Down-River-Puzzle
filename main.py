def main():
    lake_positions = {'Farmer':False,'Wolf':False,'Goat':False,'Cabbage':False}
    while True:
        display_positions(lake_positions)
        choice = input('Type what to move (or Nothing): ').lower()

        if choice.startswith('w') and can_transport_wolf_successfully(lake_positions):
            lake_positions['Farmer'] = not lake_positions['Farmer']
            lake_positions['Wolf'] = not lake_positions['Wolf']

        elif choice.startswith('g') and can_transport_goat_successfully(lake_positions):
            lake_positions['Farmer'] = not lake_positions['Farmer']
            lake_positions['Goat'] = not lake_positions['Goat']

        elif choice.startswith('c') and can_transport_cabbage_successfully(lake_positions):
            lake_positions['Farmer'] = not lake_positions['Farmer']
            lake_positions['Cabbage'] = not lake_positions['Cabbage']

        elif choice.startswith('n') and can_transport_nothing_successfully(lake_positions):
            lake_positions['Farmer'] = not lake_positions['Farmer']

        else: print('Impossible Action')

        if win_condition(lake_positions):
            print('Winner!')
            break
        print()


def display_positions(my_dict):
    print(f'Farmer:{my_dict["Farmer"]}')
    print(f'Wolf:{my_dict["Wolf"]}')
    print(f'Goat:{my_dict["Goat"]}')
    print(f'Cabbage:{my_dict["Cabbage"]}')


def can_transport_wolf_successfully(my_dict):
    """
    Returns True if the farmer and the wolf are on the same side and
    if the goat is not left on the same side as the cabbage
    """
    return my_dict['Farmer'] is my_dict['Wolf'] and \
    my_dict['Goat'] != my_dict['Cabbage']


def can_transport_goat_successfully(my_dict):
    return my_dict['Farmer'] is my_dict['Goat'] # True if on the same side


def can_transport_cabbage_successfully(my_dict):
    """
    Returns True if the farmer and the cabbage are on the same side and
    if the wolf is not left on the same side as the goat
    """
    return my_dict['Farmer'] is my_dict['Wolf'] and \
    my_dict['Wolf'] != my_dict['Goat']


def can_transport_nothing_successfully(my_dict):
    if my_dict['Wolf'] == my_dict['Goat']: return False
    if my_dict['Goat'] == my_dict['Cabbage']: return False
    return True


def win_condition(my_dict):
    return my_dict['Wolf'] == my_dict['Goat'] == my_dict['Cabbage'] == True


if __name__ == '__main__':
    main()