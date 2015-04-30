# -*- coding: utf-8 -*-

from board import Coordinate

class Player:

    def __init__(self, color):
        self._color = color
        self._game = None

    @property
    def color(self):
        return self._color

    def is_registered(self):
        return self._game is not None

    def register_game(self, game):
        self._game = game

    def has_turn(self):
        pass


class iPlayer(Player):

    EXIT_STRINGS = ("quit", "exit", "give up", "retire")

    def __init__(self, color):
        Player.__init__(self, color)

    def step(self, string):
        coord = Coordinate.from_str(string)
        return self._game.put(self, coord)

    def has_turn(self):
        print "It comes to your turn!"
        candidates = map(lambda o:str(o),
                self._game.list_available(self.color))
        print "Candidates: %s" % " ".join(candidates)
        print "Enter a coordinate."
        while True:
            try:
                print '>',
                instr = raw_input()
                if instr in iPlayer.EXIT_STRINGS:
                    self._game.set_retired(self.color)
                    return
                if self.step(instr):
                    return
            except Exception as e:
                print e
            print "Enter a correct coordinate."
