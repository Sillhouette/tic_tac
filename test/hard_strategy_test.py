import unittest
import random
import time

import src.constants as constants

from unittest.mock import Mock
from src.hard_strategy import HardStrategy
from src.board import Board
from src.processor import Processor
from src.computer_player import ComputerPlayer
from src.human_player import HumanPlayer

class HardStrategyTest(unittest.TestCase):
    def test_execute_returns_1_on_first_turn(self):
        processor = Mock(Processor)
        processor.board = Mock(Board)
        processor.board.type = constants.THREE_BY_THREE
        processor.board.turn_count.side_effect = [0]
        processor.get_valid_moves.return_value = []
        processor.board.spaces = [None] * 9
        computer_player = Mock()
        strat = HardStrategy(processor, computer_player)
        strat.load_resources()
        expected = [constants.MOVE, "9"]

        actual = strat.execute()

        self.assertEqual(expected, actual)
    
    def test_execute_appropriately_chooses_move_on_subsequent_turns(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["X", "X", None, None, "O", None, None, "O", "X"]
        processor = Processor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = HardStrategy(processor, player_2)
        expected = [constants.MOVE, "3"]

        actual = strat.execute()

        self.assertEqual(expected, actual)

    def test_get_best_move_returns_winning_move_when_avaliable(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["O", "O", None, "X", "X", None, "X", None, None]
        processor = Processor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = HardStrategy(processor, player_2)
        expected = [constants.MOVE, "3"]

        actual = strat.execute()

        self.assertEqual(expected, actual)
    
    def test_get_best_move_blocks_enemy_when_win_not_avaliable(self):
        board = Board(constants.THREE_BY_THREE)
        board.spaces = ["X", "X", None, None, "O", None, None, "O", "X"]
        processor = Processor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = HardStrategy(processor, player_2)
        expected = [constants.MOVE, "3"]

        actual = strat.execute()

        self.assertEqual(expected, actual)

    def test_load_optimal_moves_loads_moves_for_3x3_board(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        computer_player = Mock()
        strat = HardStrategy(processor, computer_player)
        expected_response_to_blank = "9"
        expected_response_to_first = "5"
        expected_response_to_ninth = "7"

        strat.load_optimal_moves()
        optimal_moves = strat.optimal_moves
        actual_response_to_blank = optimal_moves["_________"]
        actual_response_to_first = optimal_moves["________X"]
        actual_response_to_ninth = optimal_moves["_O______X"]


        self.assertEqual(expected_response_to_blank, actual_response_to_blank)
        self.assertEqual(expected_response_to_first, actual_response_to_first)
        self.assertEqual(expected_response_to_ninth, actual_response_to_ninth)

