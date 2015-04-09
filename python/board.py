# -*- coding: utf-8 -*-

import json

class Board(json.JSONEncoder):

    SIZE = (8,8)
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    def __init__(self):
        self._data = [[0] * 8 for i in xrange(8)]
        self.reset()

    def reset(self):
        self._data[3][4] = self._data[4][3] = Board.BLACK
        self._data[3][3] = self._data[4][4] = Board.WHITE

    def __str__(self):
        string = ""
        for i in range(8):
            for j in range(8):
                string += str(self._data[i][j])
            string += "\n"
        return string[:-1]

def support_board_default(o):
        if not isinstance(o, Board):
            raise TypeError(repr(o) + "is not JSON serializable")
        json = "["
        for i in range(8):
            json += "["
            for j in range(8):
                json += str(o._data[i][j]) + ","
            json = json[:-1] + "],"
        json = json[:-1] + "]"
        return json
