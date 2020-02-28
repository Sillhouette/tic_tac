import unittest

from src.three_by_three_board import ThreeByThreeBoard

class ThreeByThreeBoardTest(unittest.TestCase):
    def test_full_board(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "O", "X", "O", "O", "X", "O", "O", "X"]
        expected = True

        actual = board.full()

        self.assertEqual(expected, actual)

    def test_not_full_board(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "O", None, "O", "X", None, None, "O", "X"]
        expected = False

        actual = board.full()

        self.assertEqual(expected, actual)

    def test_update(self):
        board = ThreeByThreeBoard()
        move = "6"
        token = "O"
        expected = [None, None, None, None, None, "O", None, None, None]

        board.update(move, token)
        actual = board.spaces

        self.assertEqual(expected, actual)
        
    def test_update_2(self):
        board = ThreeByThreeBoard()
        move = "2"
        token = "X"
        expected = [None, "X", None, None, None, None, None, None, None]

        board.update(move, token)
        actual = board.spaces

        self.assertEqual(expected, actual)

    def test_turn_count(self):
        board = ThreeByThreeBoard()
        expected = 1

        board.update("1", "X")
        
        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_turn_count_2(self):
        board = ThreeByThreeBoard()
        expected = 4

        board.update("1", "X")
        board.update("2", "O")
        board.update("5", "X")
        board.update("9", "O")
        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_move_to_index(self):
        board = ThreeByThreeBoard()
        move = "5"
        expected = 4

        actual = board.move_to_index(move)

        self.assertEqual(expected, actual)

    def test_move_to_index_2(self):
        board = ThreeByThreeBoard()
        move = "9"
        expected = 8

        actual = board.move_to_index(move)

        self.assertEqual(expected, actual)

    def test_move_result(self):
        board = ThreeByThreeBoard()
        move = "5"
        token = "X"
        expected_return = None
        expected_board =  [None, None, None, None, "X", None, None, None, None]

        actual_return = board.move_result(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)

    def test_move_result_full(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "O", "X", "O", "O", "X", "O", "O", None]
        move = "9"
        token = "O"
        expected_return = "finished"
        expected_board = ["X", "O", "X", "O", "O", "X", "O", "O", "O"]

        actual_return = board.move_result(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)
