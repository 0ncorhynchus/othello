# -*- coding: utf-8 -*


class Color:
    EMPTY = 2
    BLACK = 0
    WHITE = 1

    @classmethod
    def opponent(cls, color):
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
                self.__set_piece(Color.EMPTY, Coordinate(col,row))
        self.__set_piece(Color.BLACK, Coordinate(3,4))    # d5
        self.__set_piece(Color.BLACK, Coordinate(4,3))    # e4
        self.__set_piece(Color.WHITE, Coordinate(3,3))    # d4
        self.__set_piece(Color.WHITE, Coordinate(4,4))    # e5

    def is_in_range(self, coord):
        return 0 <= coord.col < 8 and 0 <= coord.row < 8

    def at(self, coord):
        if not self.is_in_range(coord):
            raise IndexError("board index out of range")
        return self.__get_piece(coord)

    def to_list(self):
        retval = []
        for col in range(self.MAX_COLUMN):
            tmp = []
            for row in range(self.MAX_ROW):
                tmp.append(self.__get_piece(Coordinate(col,row)))
            retval.append(tmp)
        return retval

    def is_empty(self, coord):
        return self.at(coord) == Color.EMPTY

    def count(self, color):
        count = 0
        for col in range(self.MAX_COLUMN):
            for row in range(self.MAX_ROW):
                if self.__get_piece(Coordinate(col,row)) == color:
                    count += 1
        return count

    def list_reversed_in(self, color, coord, direc):
        reversed_list = []
        next_point = coord + direc
        while self.is_in_range(next_point):
            next_color = self.at(next_point)
            if next_color == Color.EMPTY:
                return []
            if next_color == color:
                return reversed_list
            reversed_list.append(next_point)
            next_point += direc
        return []

    def list_reversed(self, color, coord):
        if not self.is_in_range(coord):
            return []
        if not self.is_empty(coord):
            return []
        reversed_list = []
        for direc in self.DIRECS:
            reversed_list.extend(
                    self.list_reversed_in(color, coord, direc))
        return reversed_list

    def can_put(self, color, coord):
        return len(self.list_reversed(color, coord)) != 0

    def list_available(self, color):
        retval = []
        for col in range(self.MAX_COLUMN):
            for row in range(self.MAX_ROW):
                coord = Coordinate(col, row)
                if self.can_put(color, coord):
                    retval.append(coord)
        return retval

    def put(self, color, coord):
        reversed_list = self.list_reversed(color, coord)
        if len(reversed_list) == 0:
            return False
        self.__set_piece(color, coord)
        for rev in reversed_list:
            self.__set_piece(color, rev)
        return True

    def __set_piece(self, color, coord):
        """
        without range check
        """
        self._data[coord.col][coord.row] = color

    def __get_piece(self, coord):
        """
        without range check
        """
        return self._data[coord.col][coord.row]

    def __str__(self):
        line = '  ' + '-'*33
        row_strs = ['    a   b   c   d   e   f   g   h', line]
        for row in range(self.MAX_ROW):
            rows = [str(row+1)]
            row_str = str(row+1) + ' |'
            for col in range(self.MAX_COLUMN):
                color = self.__get_piece(Coordinate(col,row))
                if color == Color.BLACK:
                    row_str += ' X |'
                elif color == Color.WHITE:
                    row_str += ' O |'
                else:
                    row_str += '   |'
            row_strs.append(row_str)
            row_strs.append(line)
        return '\n'.join(row_strs)

    def __repr__(self):
        return str(self)

