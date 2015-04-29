# -*- coding: utf-8 -*-

from board import *

class OthelloGame:

    def __init__(self):
        self._board = Board()
        self._turn = Color.BLACK
        self._players = {}
        self._finished = False

    def is_ready(self):
        return Color.BLACK in self._players and Color.WHITE in self._players

    def has_finished(self):
        return self._finished

    def register_player(self, player):
        if player is None:
            return False
        if player.color != Color.BLACK and player.color != Color.WHITE:
            return False
        if player.color in self._players:
            return False
        player.game = self
        self._players[player.color] = player

    def get_board(self):
        return self._board.to_list()

    def get_turn(self):
        return self._players[self._turn]

    def put(self, player, coord):
        if not self.is_ready() or self.has_finished():
            return False
        if player is not self.get_turn():
            return False

        if not self._board.put(self._turn, coord):
            return False

        next_turn = Color.next(self._turn)
        if len(self._board.list_available(next_turn)) != 0:
            self._turn = next_turn
        elif len(self._board.list_available(self._turn)) == 0:
            self._turn = Color.EMPTY
            self._finished = True

        return True


