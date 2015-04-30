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

    def start(self):
        if not self.is_ready() or self.has_finished():
            return
        self.__get_current_player().has_turn()

    def register_player(self, player):
        if player is None:
            return False
        if player.color != Color.BLACK and player.color != Color.WHITE:
            return False
        if player.color in self._players:
            return False
        player.register_game(self)
        self._players[player.color] = player

    def __get_current_player(self):
        return self._players[self._turn]

    def get_board(self):
        return self._board.to_list()

    def get_turn(self):
        return self._players[self._turn]

    def put(self, player, coord):
        if not self.is_ready() or self.has_finished():
            return False
        if player is not self.__get_current_player():
            return False

        if not self._board.put(self._turn, coord):
            return False

        print self._board
        self.update_turn()
        if not self.has_finished():
            self.__get_current_player().has_turn()

        return True

    def list_available(self, color):
        return self._board.list_available(color)

    def set_retired(self, color):
        self._turn = Color.EMPTY
        self._finished = True

    def update_turn(self):
        next_turn = Color.next(self._turn)
        if len(self._board.list_available(next_turn)) != 0:
            self._turn = next_turn
        elif len(self._board.list_available(self._turn)) == 0:
            self._turn = Color.EMPTY
            self._finished = True


