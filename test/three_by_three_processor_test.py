import unittest
import src.constants as constants

from unittest.mock import Mock
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor

class ThreeByThreeProcessorTest(unittest.TestCase):
    def test_move_to_index_returns_4_when_given_5(self):
        board = Mock()
        processor = ThreeByThreeProcessor(board)
        move = "5"
        expected = 4

        actual = processor.move_to_index(move)

        self.assertEqual(expected, actual)

    def test_move_to_index_returns_8_when_given_9(self):
        board = Mock()
        processor = ThreeByThreeProcessor(board)
        move = "9"
        expected = 8

        actual = processor.move_to_index(move)

        self.assertEqual(expected, actual)

    def test_execute_move_returns_none_when_game_not_over(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        move = "5"
        token = "X"
        expected_return = None
        expected_board =  [None, None, None, None, "X", None, None, None, None]

        actual_return = processor.execute_move(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)

    def test_move_result_returns_winning_token_when_winner(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        board.spaces = ["X", "X", "O", "O", None, "X", "X", None, "X"]
        move = "8"
        token = "X"
        expected_return = "X"
        expected_board = ["X", "X", "O", "O", None, "X", "X", "X", "X"]

        actual_return = processor.execute_move(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)

    def test_current_player_returns_current_player_on_turn_5(self):
        cli = Mock()
        validator = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        processor = ThreeByThreeProcessor(board)
        processor.set_players(players)
        board.turn_count = Mock()
        board.turn_count.return_value = 5
        expected = player_2

        actual = processor.current_player()

        self.assertEqual(expected, actual)

    def test_current_player_returns_current_player_on_turn_8(self):
        cli = Mock()
        validator = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        processor = ThreeByThreeProcessor(board)
        processor.set_players(players)
        board.turn_count = Mock()
        board.turn_count.return_value = 8
        expected = player_1

        actual = processor.current_player()

        self.assertEqual(expected, actual)

    def test_move_result_returns_CATS_when_board_full(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        board.spaces = ["X", "X", "O", "O", "O", "X", "X", None, "X"]
        move = "8"
        token = "O"
        expected_return = "finished"
        expected_board = ["X", "X", "O", "O", "O", "X", "X", "O", "X"]

        actual_return = processor.execute_move(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)


    def test_get_valid_moves_returns_list_of_valid_moves_when_board_empty(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        actual = processor.get_valid_moves()

        self.assertEqual(expected, actual)
    
    def test_get_valid_moves_returns_list_of_valid_moves_when_board_not_empty(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        board.update(3, "X")
        board.update(4, "O")
        expected = [1, 2, 3, 6, 7, 8, 9]

        actual = processor.get_valid_moves()

        self.assertEqual(expected, actual)


    def test_valid_move_returns_true_when_valid(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        move = "1"
        expected = True

        actual = processor.valid_move(move)

        self.assertEqual(expected, actual)

    def test_valid_move_returns_false_when_out_of_bounds(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        move = "55"
        expected = False

        actual = processor.valid_move(move)

        self.assertEqual(expected, actual)

    def test_valid_move_returns_false_when_already_taken(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        position = 2
        board.spaces[position] = "X"
        move = "3"
        expected = False

        actual = processor.valid_move(move)

        self.assertEqual(expected, actual)

    def test_compare_board_indicies_returns_true_when_values_are_same(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        board.update(0, "X")
        board.update(1, "X")
        expected = True

        actual = processor.compare_board_indicies(0, 1)

        self.assertEqual(expected, actual)

    def test_compare_board_indicies_returns_false_when_values_are_not_same(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        board.update(1, "X")
        expected = False

        actual = processor.compare_board_indicies(0, 1)

        self.assertEqual(expected, actual)

    def test_winner_returns_winning_token_when_player_has_won(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        token = "X"
        expected = token

        board.update(0, token)
        board.update(1, token)
        board.update(2, token)
        actual = processor.winner()

        self.assertEqual(expected, actual)

    def test_winner_returns_None_when_no_winner_exists(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        token_1 = "X"
        token_2 = "O"
        X_moves = [0, 1, 5, 6, 8]
        O_moves = [2, 3, 4, 7]
        expected = None

        for move in X_moves:
            board.update(move, token_1)

        for move in O_moves:
            board.update(move, token_2)

        actual = processor.winner()

        self.assertEqual(expected, actual)
