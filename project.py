from playfair import Square


def main():
    display_main_menu()
    sq = Square("PLAYFAIR")
    # print(sq.generate_square("PLAYFAIR"))


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


def set_key():
    ...


def encode():
    ...


if __name__ == "__main__":
    main()
