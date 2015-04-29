# -*- coding: utf-8 -*-

import unittest
from board import *

class CoordinateTest(unittest.TestCase):

    def test_from_str(self):
        string = 'd3'
        coordinate = Coordinate.from_str(string)
        expected_coordinate = Coordinate(3,2)
        self.assertEqual(coordinate.col, expected_coordinate.col)
        self.assertEqual(coordinate.row, expected_coordinate.row)

class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_is_in_range(self):
        self.assertTrue(self.board.is_in_range(Coordinate(0,0)))
        self.assertTrue(self.board.is_in_range(Coordinate(7,7)))
        self.assertFalse(self.board.is_in_range(Coordinate(-1,0)))
        self.assertFalse(self.board.is_in_range(Coordinate(0,-1)))
        self.assertFalse(self.board.is_in_range(Coordinate(0,8)))
        self.assertFalse(self.board.is_in_range(Coordinate(8,0)))

    def test_is_empty(self):
        self.assertFalse(self.board.is_empty(Coordinate(3,3)))
        self.assertFalse(self.board.is_empty(Coordinate(4,4)))
        self.assertTrue(self.board.is_empty(Coordinate(5,3)))
        self.assertTrue(self.board.is_empty(Coordinate(3,5)))

    def test_at(self):
        self.assertEqual(self.board.at(Coordinate(3,3)), Color.WHITE)
        self.assertEqual(self.board.at(Coordinate(4,4)), Color.WHITE)
        self.assertEqual(self.board.at(Coordinate(4,3)), Color.BLACK)
        self.assertEqual(self.board.at(Coordinate(3,4)), Color.BLACK)
        self.assertEqual(self.board.at(Coordinate(5,3)), Color.EMPTY)

    def test_put(self):
        self.assertFalse(self.board.put(Color.WHITE,Coordinate(2,3)))
        self.assertEqual(self.board.at(Coordinate(2,3)), Color.EMPTY)
        self.assertTrue(self.board.put(Color.BLACK,Coordinate(2,3)))
        self.assertEqual(self.board.at(Coordinate(2,3)), Color.BLACK)

    def test_to_list(self):
        wanted_list = self.board.to_list()
        wanted_list[2][3] = Color.BLACK
        self.assertTrue(self.board.put(Color.BLACK,Coordinate(2,3)))
        self.assertEqual(self.board.to_list(), wanted_list)

if __name__ == "__main__":
    unittest.main()
