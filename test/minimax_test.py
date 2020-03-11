import unittest

import src.constants as constants

from unittest.mock import Mock
from src.minimax import Minimax

class MinimaxTest(unittest.TestCase):
    def test_score_move_properly_scores_max_win(self):
        processor = Mock()
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.side_effect = lambda: ["X", "O"]
        maximizer_index = 1
        maximizer_token = "O"
        minimax = Minimax(processor, maximizer_index)
        expected = 10

        actual = minimax.score_move(maximizer_token)

        self.assertEqual(expected, actual)

    def test_score_move_properly_scores_min_win(self):
        processor = Mock()
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.side_effect = lambda: ["X", "O"]
        maximizer_index = 1
        minimizer_token = "X"
        minimax = Minimax(processor, maximizer_index)
        expected = -10

        actual = minimax.score_move(minimizer_token)

        self.assertEqual(expected, actual)

    def test_score_move_properly_scores_tie(self):
        processor = Mock()
        processor.get_player_tokens = Mock()
        processor.get_player_tokens.side_effect = lambda: ["X", "O"]
        maximizer_index = 1
        minimax = Minimax(processor, maximizer_index)
        expected = 0

        actual = minimax.score_move(constants.CATS)

        self.assertEqual(expected, actual)

