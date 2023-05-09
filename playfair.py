

class Cell():

    def __init__(self, x, y, letter="Placeholder"):

        self.x = x
        self.y = y
        self.letter = letter

    def __str__(self):
        return f'{self.letter} @ [{self.x}, {self.y}]'

    def same_row(self, cell_2):
        """Returns boolean representing if the cell is in the same row as cell_2.

        Args:
            cell_2 (Cell class): Cell object of cell to compare.

        Returns:
            bool: True if cell is in the same row as cell_2
        """
        return self.y == cell_2.y

    def same_column(self, cell_2):
        """Returns boolean representing if the cell is in the same column as cell_2.

        Args:
            cell_2 (Cell class): Cell object of cell to compare.

        Returns:
            bool: True if cell is in the same column as cell_2
        """
        return self.x == cell_2.x

    @property
    def x(self):
        """Gets x coordinate of Cell

        Returns:
            int: x coordinate of Cell
        """
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        """Gets y coordinate of Cell

        Returns:
            int: y coordinate of Cell
        """
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @property
    def letter(self):
        """Gets letter character of Cell

        Returns:
            str: letter character of Cell
        """
        return self._letter

    @letter.setter
    def letter(self, new_letter):
        self._letter = new_letter


if __name__ == "__main__":
    cell1 = Cell(3, 4)
    cell2 = Cell(2, 4)
    print(cell1.same_row(cell2))
