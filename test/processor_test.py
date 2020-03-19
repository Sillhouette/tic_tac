import unittest
import src.constants as constants

from unittest.mock import Mock
from src.board import Board
from src.processor import Processor

class ProcessorTest(unittest.TestCase):
    def test_move_to_index_returns_4_when_given_5(self):
        board = Mock()
        processor = Processor(board)
        move = "5"
        expected = 4

        actual = processor.move_to_index(move)

        self.assertEqual(expected, actual)

    def test_move_to_index_returns_8_when_given_9(self):
        board = Mock()
        processor = Processor(board)
        move = "9"
        expected = 8

        actual = processor.move_to_index(move)

        self.assertEqual(expected, actual)

    def test_get_taken_positions_returns_single_taken_position(self):
        board = Board(constants.THREE_BY_THREE)
        position = 1
        board.update(position, "X")
        processor = Processor(board)
        expected = [position]

        actual = processor.get_taken_positions()

        self.assertEqual(expected, actual)

    def test_get_taken_positions_returns_taken_position_list(self):
        board = Board(constants.THREE_BY_THREE)
        positions = [1, 2, 3, 4]
        for position in positions:
            board.update(position, "X")
        processor = Processor(board)
        expected = positions

        actual = processor.get_taken_positions()

        self.assertEqual(expected, actual)

    def test_get_player_tokens_returns_player_tokens(self):
        board = Mock()
        processor = Processor(board)
        player_1, player_2 = [Mock(), Mock()]
        tokens = ["X", "O"]
        player_1.token = tokens[0]
        player_2.token = tokens[1]
        processor.set_players([player_1, player_2])
        expected = tokens

        actual = processor.get_player_tokens()

        self.assertEqual(expected, actual)

    def test_next_player_index_returns_next_players_index(self):
        board = Mock()
        processor = Processor(board)
        player_1, player_2 = [Mock(), Mock()]
        tokens = ["X", "O"]
        player_1.token = tokens[0]
        player_2.token = tokens[1]
        current_player_index = 0
        next_player_index = 1
        processor.set_players([player_1, player_2])
        expected = next_player_index

        actual = processor.next_player_index(current_player_index)

        self.assertEqual(expected, actual)

    def test_next_player_index_returns_first_players_index(self):
        board = Mock()
        processor = Processor(board)
        player_1, player_2 = [Mock(), Mock()]
        tokens = ["X", "O"]
        player_1.token = tokens[0]
        player_2.token = tokens[1]
        current_player_index = 1
        next_player_index = 0
        processor.set_players([player_1, player_2])
        expected = next_player_index

        actual = processor.next_player_index(current_player_index)

        self.assertEqual(expected, actual)

    def test_execute_move_returns_none_when_game_not_over(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        move = "5"
        token = "X"
        expected_return = None
        expected_board =  [None, None, None, None, "X", None, None, None, None]

        actual_return = processor.execute_move(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)

    def test_move_result_returns_winning_token_when_winner(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
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
        processor = Processor(board)
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
        processor = Processor(board)
        processor.set_players(players)
        board.turn_count = Mock()
        board.turn_count.return_value = 8
        expected = player_1

        actual = processor.current_player()

        self.assertEqual(expected, actual)

    def test_move_result_returns_CATS_when_board_full(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
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
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        actual = processor.get_valid_moves()

        self.assertEqual(expected, actual)
    
    def test_get_valid_moves_returns_list_of_valid_moves_when_board_not_empty(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        board.update(3, "X")
        board.update(4, "O")
        expected = [1, 2, 3, 6, 7, 8, 9]

        actual = processor.get_valid_moves()

        self.assertEqual(expected, actual)


    def test_valid_move_returns_true_when_valid(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        move = "1"
        expected = True

        actual = processor.valid_move(move)

        self.assertEqual(expected, actual)

    def test_valid_move_returns_false_when_out_of_bounds(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        move = "55"
        expected = False

        actual = processor.valid_move(move)

        self.assertEqual(expected, actual)

    def test_valid_move_returns_false_when_already_taken(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        position = 2
        board.spaces[position] = "X"
        move = "3"
        expected = False

        actual = processor.valid_move(move)

        self.assertEqual(expected, actual)

    def test_compare_board_indicies_returns_true_when_values_are_same(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        board.update(0, "X")
        board.update(1, "X")
        expected = True

        actual = processor.compare_board_indicies(0, 1)

        self.assertEqual(expected, actual)

    def test_compare_board_indicies_returns_false_when_values_are_not_same(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        board.update(1, "X")
        expected = False

        actual = processor.compare_board_indicies(0, 1)

        self.assertEqual(expected, actual)

    def test_winner_returns_winning_token_when_player_has_won(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        token = "X"
        expected = token

        board.update(0, token)
        board.update(1, token)
        board.update(2, token)
        actual = processor.winner()

        self.assertEqual(expected, actual)

    def test_winner_returns_None_when_no_winner_exists(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
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

    def test_generate_move_action_returns_proper_action_when_given_move(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        move = "5"
        expected = [constants.MOVE, move]

        actual = processor.generate_move_action(move)

        self.assertEqual(expected, actual)

    def test_generate_move_action_returns_error_action_when_given_invalid_move(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        move = "55"
        expected = [constants.ERROR, move]

        actual = processor.generate_move_action(move)

        self.assertEqual(expected, actual)

    def test_generate_move_action_returns_exit_action_when_given_exit(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        move = "exit"
        expected = [constants.EXIT, None]

        actual = processor.generate_move_action(move)

        self.assertEqual(expected, actual)

