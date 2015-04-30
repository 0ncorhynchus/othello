# -*- coding: utf-8 -*-

from player import Player
from board import Color
import random
import copy

class RandomPlayer(Player):

    def __init__(self, name, color):
        Player.__init__(self, name, color)

    def has_turn(self):
        available = self._game.list_available(self.color)
        coord = random.choice(available)
        self._game.put(self, coord)

class FirstOrderPlayer(Player):

    def __init__(self, name, color):
        Player.__init__(self, name, color)

    def has_turn(self):
        available = self._game.list_available(self.color)
        board = self._game._board
        bests = []
        max_reversed = 1
        for coord in available:
            num_reversed = len(board.list_reversed(self.color, coord))
            if num_reversed == max_reversed:
                bests.append(coord)
            elif num_reversed > max_reversed:
                bests = [coord]
                max_reversed = num_reversed
        coord = random.choice(bests)
        self._game.put(self, coord)

class MinimumPlayer(Player):

    #__init__ = Player.__init__
    def __init__(self, name, color):
        Player.__init__(self, name, color)
        self.opponent = Color.opponent(color)

    def has_turn(self):
        available = self._game.list_available(self.color)
        mins = []
        min_way = 64
        for coord in available:
            board = copy.deepcopy(self._game._board)
            board.put(self.color, coord)
            num_way = len(board.list_available(self.opponent))
            if num_way == min_way:
                mins.append(coord)
            elif num_way < min_way:
                mins = [coord]
                min_way = num_way
        coord = random.choice(mins)
        self._game.put(self, coord)

