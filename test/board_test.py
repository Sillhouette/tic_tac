import unittest

from src.board import Board

class BoardTest(unittest.TestCase):
    
    def test_full_board(self):
        board = Board()

        board.spaces = ["X", "O", "X", "O", "O", "X", "O", "O", "X"]
        
        self.assertEqual(board.full(), True)

    def test_not_full_board(self):
        board = Board()

        board.spaces = ["X", "O", None, "O", "X", None, None, "O", "X"]

        self.assertEqual(board.full(), False)

    def test_update_board(self):
        board = Board()
        expected = [None, "X", None, None, None, None, None, None, None]

        board.update(1, "X")
        actual = board.spaces

        self.assertEqual(expected, actual)


    def test_update_board_2(self):
        board = Board()
        expected = [None, None, None, None, None, "O", None, None, None]

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
    
    def test_valid_move(self):
        board = Board()
        position = 4
        expected = True

        actual = board.valid_move(position)

        self.assertEqual(expected, actual)

    def test_invalid_move(self):
        board = Board()
        position = 15
        expected = False

        actual = board.valid_move(position)

        self.assertEqual(expected, actual)

    def test_invalid_move_2(self):
        board = Board()
        position = 6
        board.spaces[position] = "X"
        expected = False

        actual = board.valid_move(position)

        self.assertEqual(expected, actual)

    def test_position_taken(self):
        board = Board()
        position = 4
        board.spaces[position] = "X"
        expected = True

        actual = board.position_taken(position)

        self.assertEqual(expected, actual)
   
    def test_position_not_taken(self):
        board = Board()
        position = 4
        expected = False

        actual = board.position_taken(position)

        self.assertEqual(expected, actual)

    def test_within_board(self):
        board = Board()
        position = 5
        expected = True

        actual = board.within_board(position)

        self.assertEqual(expected, actual)

    def test_position_out_of_bounds(self):
        board = Board()
        position = 50
        expected = False

        actual = board.within_board(position)

        self.assertEqual(expected, actual)

