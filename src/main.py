# -*- coding: utf-8 -*-

from board import Color, Coordinate
from player import iPlayer
from game import OthelloGame

def main():
    game = OthelloGame()
    player_black = iPlayer(Color.BLACK)
    player_white = iPlayer(Color.WHITE)

    game.register_player(player_black)
    game.register_player(player_white)

    game.start()


if __name__ == '__main__':
    main()
