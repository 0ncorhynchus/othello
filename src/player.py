# -*- coding: utf-8 -*-

class Player:

    def __init__(self, color):
        self._color = color
        self._game = None

    @property
    def color(self):
        return self._color

    def is_registered(self):
        return self._game is not None

    def has_turn(self):
        pass

