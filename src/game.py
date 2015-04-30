# -*- coding: utf-8 -*-

import threading
from board import *

class OthelloGame(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self._board = Board()
        self._turn = Color.BLACK
        self._players = {}
        self._winner = None
        self._finished = False

    def is_ready(self):
        return Color.BLACK in self._players and Color.WHITE in self._players

    def has_finished(self):
        return self._finished

    def print_result(self):
        print "====== RESULT ======"

        num_black = self._board.count(Color.BLACK)
        num_white = self._board.count(Color.WHITE)
        name_black = self._players[Color.BLACK].name
        name_white = self._players[Color.WHITE].name
        print "%s : %d" % (name_black, num_black)
        print "%s : %d" % (name_white, num_white)

        if self._winner is not None:
            print "Winner : %s" % self._winner.name
        elif num_black > num_white:
            print "Winner : %s" % name_black
        elif num_black < num_white:
            print "Winner : %s" % name_white
        else:
            print "Draw"

    def run(self):
        if not self.is_ready():
            return

        while not self.has_finished():
            print self._board
            self.__notice_to_player()
            self.__update_turn()

        self.print_result()

    def __notice_to_player(self):
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
        return self._board.put(self._turn, coord)

    def list_available(self, color):
        return self._board.list_available(color)

    def set_retired(self, color):
        self._turn = Color.EMPTY
        self._winner = self._players[Color.opponent(color)]
        self._finished = True

    def __update_turn(self):
        next_turn = Color.opponent(self._turn)
        if len(self._board.list_available(next_turn)) != 0:
            self._turn = next_turn
        elif len(self._board.list_available(self._turn)) == 0:
            self._turn = Color.EMPTY
            self._finished = True


