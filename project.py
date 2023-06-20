import sys
from tabulate import tabulate


def main():
    key = []

    # Processes user menu option
    user_selection = ""
    while (user_selection != 4):
        # Display main menu, wait for valid user input
        display_main_menu()
        user_selection = ask_user_menu()

        if 1 <= user_selection <= 3:
            # Sets key if one does not exist or selection is to set key
            if len(key) == 0 or user_selection == 1:
                key = menu_select_key()

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
    """_summary_

    Returns:
        _type_: _description_
    """

    VALID_OPTIONS = [1, 2, 3, 4]
    user_selection = ""
    while (user_selection not in VALID_OPTIONS):
        user_selection = input("Enter a menu option: ")

        try:
            user_selection = int(user_selection)
        except ValueError:
            print("Please enter a valid menu number option.")

    return user_selection


def menu_select_key():
    """_summary_

    Returns:
        _type_: _description_
    """
    user_key = ""
    while len(user_key) == 0:
        user_key = input("Enter a key with alphabetic characters: ")
        user_key = str_all_alpha(user_key)

        # Error message when key has no alphabet characters.
        if len(user_key) == 0:
            print("Invalid key.")

    key_preprocess = process_key_list(user_key.upper())

    key = generate_playfair_key_square(key_preprocess)
    display_table(key)
    return key


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


def process_key_list(key=""):
    """_summary_

    Args:
        key (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    ALPHA = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    pre_set_key = [*(key + ALPHA)]
    return list(dict.fromkeys(pre_set_key))


def generate_playfair_key_square(alpha_key_list):
    square_list = []

    for index, char in enumerate(alpha_key_list):
        x_coord = index % 5
        y_coord = index // 5

        new_cell = {
            'x': x_coord,
            'y': y_coord,
            'index': y_coord * 5 + x_coord,
            'letter': char
        }

        square_list.append(new_cell)

    return square_list


def str_all_alpha(str):
    """
    Receives input string, returns the input string where all characters which
    are not part of the alphabet removed. The characters are all capitalized.

    Args:
        message (str): _description_

    Returns:
        str: _description_
    """
    return ''.join(ch for ch in str if ch.isalpha())


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
        ...

    print(tabulate(table))
    ...


def ask_user_message():
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
    """_summary_

    Args:
        cell (_type_): _description_

    Returns:
        _type_: _description_
    """
    return y * 5 + x


if __name__ == "__main__":
    main()
