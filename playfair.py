# I = J


class Square():
    def __init__(self, key="ABCDEFGHIKLMNOPQRSTUVWXYZ"):

        self.key = key
        self.key_square = self.generate_square(key)
        ...

    def __str__(self):
        # TODO
        # String representaion of key
        return "ABC"

    def clean_key(self, key):
        return key.replace(" ", "").upper()

    def generate_square(self, key):
        PF_ALPHA = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I = J

        # Generate alphabetical list of chars
        alpha_list = []
        for char in PF_ALPHA:
            alpha_list.append(char)

        # Generate list of chars from key to make set from
        key_alpha_list = []
        for char in PF_ALPHA:
            key_alpha_list.append(key)

        key_set = set(key_alpha_list)

        return key_set

    def display_square(self):
        ...

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key_str):
        self._key = key_str

    @property
    def key_square(self):
        return self._key_square

    @key_square.setter
    def key_square(self, key_str):
        self._key_square = self.generate_square(key_str)
