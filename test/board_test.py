import unittest
import src.constants as constants

from src.board import Board

class BoardTest(unittest.TestCase):
    def test_setup_3d_board_sets_size_to_27(self):
        board = Board(constants.THREE_DIMENSIONAL)
        expected = 27

        actual = board.size

        self.assertEqual(expected, actual)
    
    def test_setup_3x3_board_sets_size_to_9(self):
        board = Board(constants.THREE_BY_THREE)
        expected = 9

        actual = board.size

        self.assertEqual(expected, actual)


    def test_full_board(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["X", "O", "X", "O", "O", "X", "O", "O", "X"]
        expected = True

        actual = board.full()

        self.assertEqual(expected, actual)

    def test_not_full_board(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["X", "O", None, "O", "X", None, None, "O", "X"]
        expected = False

        actual = board.full()

        self.assertEqual(expected, actual)

    def test_update_board_places_token_correctly(self):
        board = Board(constants.THREE_BY_THREE)
        index = 5
        token = "O"
        expected = [None, None, None, None, None, "O", None, None, None]

        board.update(index, token)
        actual = board.spaces

        self.assertEqual(expected, actual)
        
    def test_update_board_places_different_token_correctly(self):
        board = Board(constants.THREE_BY_THREE)
        index = 1
        token = "X"
        expected = [None, "X", None, None, None, None, None, None, None]

        board.update(index, token)
        actual = board.spaces

        self.assertEqual(expected, actual)

    def test_turn_count_returns_correctly_when_one_turn_made(self):
        board = Board(constants.THREE_BY_THREE)
        index = 1
        token = "X"
        expected = 1

        board.update(index, token)
        
        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_turn_count_returns_correctly_when_four_turns_made(self):
        board = Board(constants.THREE_BY_THREE)
        expected = 4

        board.update(1, "X")
        board.update(2, "O")
        board.update(5, "X")
        board.update(8, "O")
        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_within_board_returns_true_when_within_board(self):
        board = Board(constants.THREE_BY_THREE)
        position = 0
        expected = True

        actual = board.within_board(position)

        self.assertEqual(expected, actual)

    def test_within_board_returns_true_when_given_9(self):
        board = Board(constants.THREE_BY_THREE)
        position = 9
        expected = True

        actual = board.within_board(position)

        self.assertEqual(expected, actual)

    def test_within_board_returns_false_when_not_within_board(self):
        board = Board(constants.THREE_BY_THREE)
        position = 55
        expected = False

        actual = board.within_board(position)

        self.assertEqual(expected, actual)

    def test_position_taken_retuns_false_when_not_taken(self):
        board = Board(constants.THREE_BY_THREE)
        position = 0
        expected = False

        actual = board.position_taken(position)

        self.assertEqual(expected, actual)

    def test_position_taken_returns_true_when_taken(self):
        board = Board(constants.THREE_BY_THREE)
        position = 0
        board.spaces[position] = "X"
        expected = True

        actual = board.position_taken(position)

        self.assertEqual(expected, actual)
