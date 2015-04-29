# -*- coding: utf-8 -*


class Color:
    EMPTY = 2
    BLACK = 0
    WHITE = 1

    @classmethod
    def next(cls, color):
        if color == Color.BLACK:
            return Color.WHITE
        if color == Color.WHITE:
            return Color.BLACK
        return Color.EMPTY


class Coordinate:
    def __init__(self, col, row):
        self._col = col
        self._row = row

    @property
    def col(self):
        return self._col

    @property
    def row(self):
        return self._row

    @classmethod
    def from_str(cls, string):
        if len(string) != 2:
            return None
        col_char = string[0]
        row_char = string[1]
        col = ord(col_char)-ord('a')
        row = int(row_char)-1
        return Coordinate(col, row)

    def __add__(self, other):
        if not isinstance(other, list) and not isinstance(other, tuple):
            raise TypeError("")
        if len(other) != 2:
            raise TypeError("")
        return Coordinate(self.col + other[0],
                self.row + other[1])

    def __str__(self):
        col_str = chr(self.col + ord('a'))
        row_str = str(self.row + 1)
        return col_str + row_str

    def __repr__(self):
        return str(self)


class Board:

    MAX_COLUMN = 8
    MAX_ROW = 8
    DIRECS = [(-1,-1), (0,-1), (1,-1), (-1,0),
            (1,0), (-1,1), (0,1), (1,1)]

    def __init__(self):
        self._data = [[Color.EMPTY] * 8 for i in xrange(8)]
        self.reset()

    def reset(self):
        for col in range(self.MAX_COLUMN):
            for row in range(self.MAX_ROW):
                self.put(Color.EMPTY, Coordinate(col,row))
        self._data[3][4] = self._data[4][3] = Color.BLACK
        self._data[3][3] = self._data[4][4] = Color.WHITE

    def is_in_range(self, coord):
        return 0 <= coord.col < 8 and 0 <= coord.row < 8

    def at(self, coord):
        if not self.is_in_range(coord):
            raise IndexError("board index out of range")
        return self._data[coord.col][coord.row]

    def to_list(self):
        retval = []
        for col in range(self.MAX_COLUMN):
            tmp = []
            for row in range(self.MAX_ROW):
                tmp.append(self._data[col][row])
            retval.append(tmp)
        return retval

    def is_empty(self, coord):
        return self.at(coord) == Color.EMPTY

    def can_put_with_direction(self, color, coord, direc):
        exist_other = False
        next_point = coord + direc
        while self.is_in_range(next_point):
            if self.is_empty(next_point):
                return False
            next_color = self.at(next_point)
            if not exist_other and next_color != color:
                exist_other = True
            if next_color == color:
                return exist_other
            next_point += direc
        return False

    def can_put(self, color, coord):
        if not self.is_in_range(coord):
            return False
        if not self.is_empty(coord):
            return False
        for direc in self.DIRECS:
            if self.can_put_with_direction(color, coord, direc):
                return True
        return False

    def list_available(self, color):
        retval = []
        for col in range(self.MAX_COLUMN):
            for row in range(self.MAX_ROW):
                coord = Coordinate(col, row)
                if self.can_put(color, coord):
                    retval.append(coord)
        return retval

    def put(self, color, coord):
        if not self.can_put(color, coord):
            return False
        self._data[coord.col][coord.row] = color
        return True

    def __str__(self):
        row_strs = ['  a b c d e f g h']
        for row in range(self.MAX_ROW):
            rows = [str(row+1)]
            for col in range(self.MAX_COLUMN):
                color = self._data[col][row]
                if color == Color.BLACK:
                    rows.append('X')
                elif color == Color.WHITE:
                    rows.append('O')
                else:
                    rows.append(' ')
            row_strs.append(' '.join(rows))
        return '\n'.join(row_strs)

    def __repr__(self):
        return str(self)

