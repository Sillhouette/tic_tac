import unittest

import src.constants as constants

from unittest.mock import Mock
from src.minimax import Minimax
from src.board import Board
from src.processor import Processor
from src.data_gatherer import DataGatherer

class MinimaxTest(unittest.TestCase):
    def test_calculate_score_properly_scores_max_win(self):
        processor = Mock()
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.side_effect = lambda: ["X", "O"]
        maximizer_index = 1
        maximizer_token = "O"
        minimax = Minimax(processor, maximizer_index)
        expected = 10

        actual = minimax.calculate_score(maximizer_token)

        self.assertEqual(expected, actual)

    def test_calculate_score_properly_scores_min_win(self):
        processor = Mock()
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.side_effect = lambda: ["X", "O"]
        maximizer_index = 1
        minimizer_token = "X"
        minimax = Minimax(processor, maximizer_index)
        expected = -10

        actual = minimax.calculate_score(minimizer_token)

        self.assertEqual(expected, actual)

    def test_calculate_score_properly_scores_tie(self):
        processor = Mock()
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.side_effect = lambda: ["X", "O"]
        maximizer_index = 1
        minimax = Minimax(processor, maximizer_index)
        expected = 0

        actual = minimax.calculate_score(constants.CATS)

        self.assertEqual(expected, actual)

    def test_stores_the_best_move_given_a_nearly_full_board_state(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["X", "X", "O", "O", "O", "X", "X", "O", None]
        processor = Processor(board)
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.return_value = ["X", "O"]
        processor.players = [Mock(), Mock()]
        maximizer_index = 0
        data_gatherer = DataGatherer()
        data_gatherer.store_result = Mock()
        minimax = Minimax(processor, maximizer_index, data_gatherer=data_gatherer)
        move = "9"

        minimax.get_best_move(0, maximizer_index)

        data_gatherer.store_result.assert_called_with(board.spaces, "9", False)

    def test_stores_the_best_move_given_a_board_state_with_win_avaliable(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["X", "X", "O", "X", "O", None, None, None, None]
        processor = Processor(board)
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.return_value = ["X", "O"]
        processor.players = [Mock(), Mock()]
        maximizer_index = 1
        data_gatherer = DataGatherer()
        data_gatherer.store_result = Mock()
        minimax = Minimax(processor, maximizer_index, data_gatherer=data_gatherer)

        minimax.get_best_move(0, maximizer_index)

        data_gatherer.store_result.assert_called_with(board.spaces, "7", False)

    def test_stores_the_best_move_given_a_board_state_with_win_over_block(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["O", None, "O", None, None, None, "X", None, "X"]
        processor = Processor(board)
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.return_value = ["X", "O"]
        processor.players = [Mock(), Mock()]
        maximizer_index = 0
        data_gatherer = DataGatherer()
        data_gatherer.store_result = Mock()
        minimax = Minimax(processor, maximizer_index, data_gatherer=data_gatherer)

        minimax.get_best_move(0, maximizer_index)
        
        data_gatherer.store_result.assert_called_with(board.spaces, "8", False)
    
    def test_stores_the_best_move_given_a_tie_state(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["X", None, "O", None, None, None, None, "X", "O"]
        processor = Processor(board)
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.return_value = ["X", "O"]
        processor.players = [Mock(), Mock()]
        maximizer_index = 0
        data_gatherer = DataGatherer()
        data_gatherer.store_result = Mock()
        minimax = Minimax(processor, maximizer_index, data_gatherer=data_gatherer)

        minimax.get_best_move(0, maximizer_index)
        
        data_gatherer.store_result.assert_called_with(board.spaces, "6", False)

    def test_stores_the_best_move_given_a_no_win(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["O", None, "X", None, None, None, None, None, None]
        processor = Processor(board)
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.return_value = ["X", "O"]
        processor.players = [Mock(), Mock()]
        maximizer_index = 0
        data_gatherer = DataGatherer()
        data_gatherer.store_result = Mock()
        minimax = Minimax(processor, maximizer_index, data_gatherer=data_gatherer)

        minimax.get_best_move(0, maximizer_index)
        
        data_gatherer.store_result.assert_called_with(board.spaces, "9", False)

