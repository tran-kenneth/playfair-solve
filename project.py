from playfair import Cell


def main():

    key_list = generate_playfair_key_square(
        process_key_list("PLAYFAIREXAMPLE"))
    # print(key_list)
    ...


def display_main_menu():
    DISPLAY = [
        "Playfair Cipher App",
        "",
        "1. Set a key",
        "2. Encrypt a string",
        "3. Decrypt a string",
        ""
    ]

    for line in DISPLAY:
        print(line)


def decode():
    ...


def process_key_list(key=""):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # TODO clean key input

    pre_set_key = [*(key + alphabet)]

    return list(dict.fromkeys(pre_set_key))


def generate_playfair_key_square(alpha_key_list):
    square_list = []

    for index, char in enumerate(alpha_key_list):
        x_coord = index % 5
        y_coord = index // 5

        new_cell = Cell(x_coord, y_coord, char)
        square_list.append(new_cell)

    print([str(cell) for cell in square_list])


def encode():
    ...


if __name__ == "__main__":
    main()
