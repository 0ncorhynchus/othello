# -*- coding: utf-8 -*-

from player import Player
import random

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

