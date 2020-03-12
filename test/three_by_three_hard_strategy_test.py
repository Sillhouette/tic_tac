import unittest

import src.constants as constants

from unittest.mock import Mock
from src.three_by_three_hard_strategy import ThreeByThreeHardStrategy
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor
from src.computer_player import ComputerPlayer
from src.human_player import HumanPlayer

class ThreeByThreeHardStrategyTest(unittest.TestCase):
    def test_execute_returns_1_on_first_turn(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.turn_count = Mock()
        processor.board.turn_count.side_effect = [0]
        computer_player = Mock()
        strat = ThreeByThreeHardStrategy(processor, computer_player)
        expected = [constants.MOVE, "1"]

        actual = strat.execute()

        self.assertEqual(expected, actual)

    def test_execute_returns_appropriately_on_second_turn(self):
        SECOND_MOVE = {
            0: "5",
            1: "1",
            2: "5",
            3: "1",
            4: "1",
            5: "3",
            6: "5",
            7: "2",
            8: "5"
        }
        processor = Mock()
        processor.board = Mock()
        processor.board.turn_count = Mock()
        processor.board.turn_count.side_effect = [1] * 9
        side_effects = [[key] for key in SECOND_MOVE.keys()]
        processor.get_taken_positions.side_effect = side_effects 
        computer_player = Mock()
        strat = ThreeByThreeHardStrategy(processor, computer_player)

        for value in SECOND_MOVE.values():
            expected = [constants.MOVE, value]
            
            actual = strat.execute()

            self.assertEqual(expected, actual)
    
    def test_execute_appropriately_chooses_move_on_subsequent_turns(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "X", None, None, "O", None, None, "O", "X"]
        processor = ThreeByThreeProcessor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = ThreeByThreeHardStrategy(processor, player_2)
        expected = [constants.MOVE, "3"]

        actual = strat.execute()

        self.assertEqual(expected, actual)

    def test_get_best_move_returns_winning_move_when_avaliable(self):
        board = ThreeByThreeBoard()
        board.spaces = ["O", "O", None, "X", "X", None, "X", None, None]
        processor = ThreeByThreeProcessor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = ThreeByThreeHardStrategy(processor, player_2)
        strat.set_minimax()
        expected = [constants.MOVE, "3"]

        actual = strat.get_best_move()

        self.assertEqual(expected, actual)
    
    def test_get_best_move_blocks_enemy_when_win_not_avaliable(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "X", None, None, "O", None, None, "O", "X"]
        processor = ThreeByThreeProcessor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = ThreeByThreeHardStrategy(processor, player_2)
        strat.set_minimax()
        expected = [constants.MOVE, "3"]

        actual = strat.get_best_move()

        self.assertEqual(expected, actual)

