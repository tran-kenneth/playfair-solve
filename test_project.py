import pytest
import project as pf


def test_index():
    assert pf.index_from_xy(0, 0) == 0
    assert pf.index_from_xy(1, 1) == 6
    assert pf.index_from_xy(2, 2) == 12
    assert pf.index_from_xy(3, 3) == 18
    assert pf.index_from_xy(4, 4) == 24


def test_str_all_alpha():
    assert pf.str_all_alpha('123') == ''
    assert pf.str_all_alpha('abc') == 'abc'
    assert pf.str_all_alpha('123abc') == 'abc'
    assert pf.str_all_alpha('1a2b3c') == 'abc'
    assert pf.str_all_alpha('!@#$') == ''
    assert pf.str_all_alpha('\\n') == 'n'


def test_key_to_set_list():
    ALPHA = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    assert pf.key_to_set_list(ALPHA) == [*(ALPHA)]
    assert pf.key_to_set_list("") == [*(ALPHA)]
    assert pf.key_to_set_list("DEF") == [*("DEF" + ALPHA[:3] + ALPHA[6:])]
    assert pf.key_to_set_list("WXYZ") == [*("WXYZ" + ALPHA[:-4])]
    assert pf.key_to_set_list("J") == [*("I" + ALPHA[:8] + ALPHA[9:])]


def test_square_list_from_key():
    assert pf.square_list_from_key([*("PLAYFIR" + "BCDEGHKMNOQSTUVWXZ")]) == [{'x': 0, 'y': 0, 'index': 0, 'letter': 'P'}, {'x': 1, 'y': 0, 'index': 1, 'letter': 'L'}, {'x': 2, 'y': 0, 'index': 2, 'letter': 'A'}, {'x': 3, 'y': 0, 'index': 3, 'letter': 'Y'}, {'x': 4, 'y': 0, 'index': 4, 'letter': 'F'}, {'x': 0, 'y': 1, 'index': 5, 'letter': 'I'}, {'x': 1, 'y': 1, 'index': 6, 'letter': 'R'}, {'x': 2, 'y': 1, 'index': 7, 'letter': 'B'}, {'x': 3, 'y': 1, 'index': 8, 'letter': 'C'}, {'x': 4, 'y': 1, 'index': 9, 'letter': 'D'}, {'x': 0, 'y': 2, 'index': 10, 'letter': 'E'}, {'x': 1, 'y': 2, 'index': 11, 'letter': 'G'}, {
        'x': 2, 'y': 2, 'index': 12, 'letter': 'H'}, {'x': 3, 'y': 2, 'index': 13, 'letter': 'K'}, {'x': 4, 'y': 2, 'index': 14, 'letter': 'M'}, {'x': 0, 'y': 3, 'index': 15, 'letter': 'N'}, {'x': 1, 'y': 3, 'index': 16, 'letter': 'O'}, {'x': 2, 'y': 3, 'index': 17, 'letter': 'Q'}, {'x': 3, 'y': 3, 'index': 18, 'letter': 'S'}, {'x': 4, 'y': 3, 'index': 19, 'letter': 'T'}, {'x': 0, 'y': 4, 'index': 20, 'letter': 'U'}, {'x': 1, 'y': 4, 'index': 21, 'letter': 'V'}, {'x': 2, 'y': 4, 'index': 22, 'letter': 'W'}, {'x': 3, 'y': 4, 'index': 23, 'letter': 'X'}, {'x': 4, 'y': 4, 'index': 24, 'letter': 'Z'}]

    assert pf.square_list_from_key([*("ABCDEFGHIKLMNOPQRSTUVWXYZ")]) == [{'x': 0, 'y': 0, 'index': 0, 'letter': 'A'}, {'x': 1, 'y': 0, 'index': 1, 'letter': 'B'}, {'x': 2, 'y': 0, 'index': 2, 'letter': 'C'}, {'x': 3, 'y': 0, 'index': 3, 'letter': 'D'}, {'x': 4, 'y': 0, 'index': 4, 'letter': 'E'}, {'x': 0, 'y': 1, 'index': 5, 'letter': 'F'}, {'x': 1, 'y': 1, 'index': 6, 'letter': 'G'}, {'x': 2, 'y': 1, 'index': 7, 'letter': 'H'}, {'x': 3, 'y': 1, 'index': 8, 'letter': 'I'}, {'x': 4, 'y': 1, 'index': 9, 'letter': 'K'}, {'x': 0, 'y': 2, 'index': 10, 'letter': 'L'}, {'x': 1, 'y': 2, 'index': 11, 'letter': 'M'}, {
        'x': 2, 'y': 2, 'index': 12, 'letter': 'N'}, {'x': 3, 'y': 2, 'index': 13, 'letter': 'O'}, {'x': 4, 'y': 2, 'index': 14, 'letter': 'P'}, {'x': 0, 'y': 3, 'index': 15, 'letter': 'Q'}, {'x': 1, 'y': 3, 'index': 16, 'letter': 'R'}, {'x': 2, 'y': 3, 'index': 17, 'letter': 'S'}, {'x': 3, 'y': 3, 'index': 18, 'letter': 'T'}, {'x': 4, 'y': 3, 'index': 19, 'letter': 'U'}, {'x': 0, 'y': 4, 'index': 20, 'letter': 'V'}, {'x': 1, 'y': 4, 'index': 21, 'letter': 'W'}, {'x': 2, 'y': 4, 'index': 22, 'letter': 'X'}, {'x': 3, 'y': 4, 'index': 23, 'letter': 'Y'}, {'x': 4, 'y': 4, 'index': 24, 'letter': 'Z'}]


def process_key():
    ...
