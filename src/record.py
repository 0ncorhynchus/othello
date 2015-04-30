# -*- coding: utf-8 -*-

from board import *
from player import *

class Record:

    def __init__(self, game):
        self._game = game
        self._player_black = Player(Color.BLACK)
        self._player_white = Player(Color.WHITE)
        self._game.register_player(self._player_black)
        self._game.register_player(self._player_white)

    def step(self, string):
        coord = Coordinate.from_str(string)
        return self._game.put(self._game.get_turn(), coord)

    def list_available(self):
        return self._game._board.list_available(self._game._turn)


def main():
    from game import OthelloGame
    game = OthelloGame()
    record = Record(game)
    print "Enter 'quit' to quit game"
    while not game.has_finished():
        print ""
        print "Enter a coordinate"
        candidates = map(lambda o:str(o),
                game.list_available(game.get_turn().color))
        print "Candidates: %s" % " ".join(candidates)
        try:
            print '>',
            step = raw_input()
            if step == "quit":
                break
            if record.step(step):
                print game._board
        except:
            continue

if __name__ == '__main__':
    main()
