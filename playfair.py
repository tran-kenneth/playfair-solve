
class Square():
    def __init__(self, key="ABCDEFGHIKLMNOPQRSTUVWXYZ"):

        self.key = key

    def __str__(self):
        # TODO
        # String representaion of key
        return "ABC"

    def clean_key(self, key):
        return key.replace(" ", "").upper()

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key_str):
        self._key = key_str


class Cell():

    def __init__(self, x, y, letter="Placeholder"):

        self.x = x
        self.y = y
        self.letter = letter

    def __str__(self):
        return f'{self.letter} @ [{self.x}, {self.y}]'

    def same_row(self, cell_2):
        return self.y == cell_2.y

    def same_column(self, cell_2):
        return self.x == cell_2.x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, new_letter):
        self._letter = new_letter


cell1 = Cell(3, 4)
cell2 = Cell(2, 4)
print(cell1.same_row(cell2))
