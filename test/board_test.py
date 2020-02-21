import unittest

from src.board import Board

class BoardTest(unittest.TestCase):
    
    def test_full_board(self):
        board = Board()

        board.spaces = ["X", "O", "X", "O", "O", "X", "O", "O", "X"]
        
        self.assertEqual(board.full(), True)

    def test_not_full_board(self):
        board = Board()

        board.spaces = ["X", "O", " ", "O", "X", " ", " ", "O", "X"]

        self.assertEqual(board.full(), False)

    def test_update_board(self):
        board = Board()
        expected = [" ", "X", " ", " ", " ", " ", " ", " ", " "]

        board.update(1, "X")
        actual = board.spaces

        self.assertEqual(expected, actual)


    def test_update_board_2(self):
        board = Board()
        expected = [" ", " ", " ", " ", " ", "O", " ", " ", " "]

        board.update(5, "O")
        actual = board.spaces

        self.assertEqual(expected, actual)

    def test_turn_count(self):
        board = Board()
        expected = 1

        board.update(1, "X")

        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_turn_count_2(self):
        board = Board()
        expected = 4

        board.update(1, "X")
        board.update(8, "O")
        board.update(3, "X")
        board.update(6, "O")

        actual = board.turn_count()

        self.assertEqual(expected, actual)
