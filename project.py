import sys
from tabulate import tabulate


def main():
    key = []

    # Processes user menu option
    user_selection = ""
    while (user_selection != 4):
        # Displays main menu and waits for valid user input
        display_main_menu()
        user_selection = ask_user_menu()

        if 1 <= user_selection <= 3:
            # Sets key if one does not exist or selection is to set key
            if len(key) == 0 or user_selection == 1:
                user_key_to_process = ask_user_key()
                key = process_key(user_key_to_process)

            # Process to encode or decode based on user selection
            if user_selection == 2:
                menu_select_encode(key)
            elif user_selection == 3:
                menu_select_decode(key)

    sys.exit()


def display_main_menu():
    """_summary_
    """
    DISPLAY = [
        "Playfair Cipher App",
        "",
        "1. Set a key",
        "2. Encrypt a string",
        "3. Decrypt a string",
        "4. Exit",
        ""
    ]

    for line in DISPLAY:
        print(line)


def ask_user_menu():
    """Asks user for to select a valid menu option in the form of a number.

    Returns:
        int: User selected number option on the menu.
    """

    user_selection = ""
    VALID_OPTIONS = [1, 2, 3, 4]

    # Loops until user selects a valid number option.
    while (user_selection not in VALID_OPTIONS):
        user_selection = input("Enter a menu option: ")

        # Try to convert string entry into a integer
        try:
            user_selection = int(user_selection)
        except ValueError:
            print("Please enter a valid menu number option.\n")

    return user_selection


def ask_user_key():
    user_key = ""
    while len(user_key) == 0:
        user_key = input("Enter a key with alphabetic characters: ")
        user_key = str_all_alpha(user_key)

        # Error message when key has no alphabet characters.
        if len(user_key) == 0:
            print("Invalid key.\n")

    return user_key


def str_all_alpha(str):
    """
    Receives input string, returns the input string where all characters which
    are not part of the alphabet removed.

    Args:
        str (str): String input which may contain any character(letter, num, punctuation etc.)

    Returns:
        str: String containing only letters of the alphabet.
    """
    return ''.join(ch for ch in str if ch.isalpha())


def process_key(user_key):
    """_summary_

    Args:
        user_key (_type_): _description_

    Returns:
        _type_: _description_
    """
    key_set_list = key_to_set_list(user_key.upper())

    key = square_list_from_key(key_set_list)
    display_table(key)
    return key


def key_to_set_list(key):
    """_summary_

    Args:
        key (_type_): _description_

    Returns:
        list: _description_
    """

    # Alphabet for playfair 5 x 5 square. I=J for his variation.
    ALPHA = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    pre_set_key = [*(key.replace("J", "I") + ALPHA)]
    return list(dict.fromkeys(pre_set_key))


def square_list_from_key(key_set_list):
    """_summary_

    Args:
        key_set_list (_type_): _description_

    Returns:
        list: _description_
    """
    square_list = []

    for index, char in enumerate(key_set_list):
        x_coord = index % 5
        y_coord = index // 5

        # Cell in 5 x 5 grid of playfair square to add into list
        new_cell = {
            'x': x_coord,
            'y': y_coord,
            'index': y_coord * 5 + x_coord,
            'letter': char
        }

        square_list.append(new_cell)

    print(square_list)
    return square_list


def menu_select_encode(key):
    user_message = ask_user_message()

    message_letter_pairs = pair_letters(user_message)
    print(message_letter_pairs)

    result = ""
    for pair in message_letter_pairs:
        char_1 = pair[:1]
        char_2 = pair[1:]

        for cell in key:
            if cell["letter"] == char_1:
                cell_char_1 = cell
            if cell["letter"] == char_2:
                cell_char_2 = cell

        print(cell_char_1, cell_char_2)
        # Same row, different column
        if (is_same_row(cell_char_1, cell_char_2)):
            new_index_1 = encode_in_row(cell_char_1)
            new_index_2 = encode_in_row(cell_char_2)
            new_pair = key[new_index_1]['letter'] + key[new_index_2]['letter']
            result += new_pair

        # Same column, different row
        elif (is_same_column(cell_char_1, cell_char_2)):
            new_index_1 = encode_in_column(cell_char_1)
            new_index_2 = encode_in_column(cell_char_2)
            new_pair = key[new_index_1]['letter'] + key[new_index_2]['letter']
            result += new_pair
        # Different row, different column
        else:
            new_index_1, new_index_2 = encode_in_box(cell_char_1, cell_char_2)
            new_pair = key[new_index_1]['letter'] + key[new_index_2]['letter']
            result += new_pair

    print(result)
    return result


def menu_select_decode(key):
    user_message = ask_user_message()

    message_letter_pairs = pair_letters(user_message)
    print(message_letter_pairs)

    result = ""
    for pair in message_letter_pairs:
        char_1 = pair[:1]
        char_2 = pair[1:]

        for cell in key:
            if cell["letter"] == char_1:
                cell_char_1 = cell
            if cell["letter"] == char_2:
                cell_char_2 = cell

        print(cell_char_1, cell_char_2)
        # Same row, different column
        if (is_same_row(cell_char_1, cell_char_2)):
            new_index_1 = decode_in_row(cell_char_1)
            new_index_2 = decode_in_row(cell_char_2)
            new_pair = key[new_index_1]['letter'] + key[new_index_2]['letter']
            result += new_pair

        # Same column, different row
        elif (is_same_column(cell_char_1, cell_char_2)):
            new_index_1 = decode_in_column(cell_char_1)
            new_index_2 = decode_in_column(cell_char_2)
            new_pair = key[new_index_1]['letter'] + key[new_index_2]['letter']
            result += new_pair
        # Different row, different column
        else:
            new_index_1, new_index_2 = decode_in_box(cell_char_1, cell_char_2)
            new_pair = key[new_index_1]['letter'] + key[new_index_2]['letter']
            result += new_pair

    print(result)
    return result


def display_table(key):
    table = []

    row_count = 0
    temp_row = []
    for entry in key:
        letter = f'{entry["letter"]} {entry["index"]}'
        temp_row.append(letter)
        row_count += 1
        if (row_count == 5):
            table.append(temp_row)
            temp_row = []
            row_count = 0

    print(tabulate(table))


def ask_user_message():
    """_summary_

    Returns:
        _type_: _description_
    """
    user_message = ""
    while len(user_message) == 0:
        user_message = input("Enter message to encode/decode: ")
        user_message = str_all_alpha(user_message)

        # Error message when key has no alphabet characters.
        if len(user_message) == 0:
            print("Enter at least 1 alphabet character.")

    return user_message.upper()


def pair_letters(message):
    letter_pairs = []

    num_chars = len(message)

    char_index = 0
    while (char_index < num_chars):
        char_1 = message[char_index:char_index+1]
        char_2 = message[char_index+1:char_index+2]

        if (char_1 == char_2 or not char_2):
            pair = char_1 + 'X'
            char_index += 1
            ...
        else:
            pair = char_1 + char_2
            char_index += 2
            ...

        letter_pairs.append(pair)

    return letter_pairs


def is_same_row(cell_1, cell_2):
    return cell_1['y'] == cell_2['y']


def is_same_column(cell_1, cell_2):
    return cell_1['x'] == cell_2['x']


def encode_in_column(cell_1):
    cell_1_index = cell_1['index']
    new_letter_index = cell_1_index + 5

    if (new_letter_index > 24):
        new_letter_index = new_letter_index % 24 - 1

    return new_letter_index


def encode_in_row(cell_1):
    cell_1_index = cell_1['index']
    new_letter_index = cell_1_index + 1

    if (new_letter_index % 5 == 0):
        new_letter_index = new_letter_index - 5

    return new_letter_index


def encode_in_box(cell_1, cell_2):
    x_1, y_1 = cell_1['x'], cell_1['y']
    x_2, y_2 = cell_2['x'], cell_2['y']

    new_x_1, new_y_1 = x_2, y_1
    new_x_2, new_y_2 = x_1, y_2

    new_index_1 = index_from_xy(new_x_1, new_y_1)
    new_index_2 = index_from_xy(new_x_2, new_y_2)

    return (new_index_1, new_index_2)


def decode_in_column(cell_1):
    cell_1_index = cell_1['index']
    new_letter_index = cell_1_index - 5

    if (new_letter_index < 0):
        new_letter_index += 25

    return new_letter_index


def decode_in_row(cell_1):
    cell_1_index = cell_1['index']
    new_letter_index = cell_1_index - 1

    if (new_letter_index % 5 == 4):
        new_letter_index = new_letter_index + 5

    return new_letter_index


def decode_in_box(cell_1, cell_2):
    x_1, y_1 = cell_1['x'], cell_1['y']
    x_2, y_2 = cell_2['x'], cell_2['y']

    new_x_1, new_y_1 = x_2, y_1
    new_x_2, new_y_2 = x_1, y_2

    new_index_1 = index_from_xy(new_x_1, new_y_1)
    new_index_2 = index_from_xy(new_x_2, new_y_2)

    return (new_index_1, new_index_2)


def index_from_xy(x, y):
    """Returns an index in a 25 length list which represents a 5 x 5 grid.

    Args:
        x (int): Location on the x axis.
        y (int): Location on the y axis.

    Returns:
        int: Index in a 25 length list.
    """
    return y * 5 + x


if __name__ == "__main__":
    main()
