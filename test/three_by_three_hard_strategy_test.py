import unittest
import random
import time

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
        expected = [constants.MOVE, "3"]

        actual = strat.execute()

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
        expected = [constants.MOVE, "3"]

        actual = strat.execute()

        self.assertEqual(expected, actual)

    def test_computer_makes_instantaneous_fourth_move(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", None, "X", None, "O", None, None, None, None]
        processor = ThreeByThreeProcessor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = ThreeByThreeHardStrategy(processor, player_2)
        expected = 0.06

        actual = self.benchmark(strat.execute)

        self.assertGreaterEqual(expected, actual)

    def test_computer_makes_instantaneous_second_move(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", None, None, None, None, None, None, None, None]
        processor = ThreeByThreeProcessor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = ThreeByThreeHardStrategy(processor, player_2)
        expected = 0.06

        actual = self.benchmark(strat.execute)

        self.assertGreaterEqual(expected, actual)

    def test_computer_makes_instantaneous_moves(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = ThreeByThreeHardStrategy(processor, player_2)
        num_turns_until_algorithm = range(2)
        expected = 0.5
        actuals = []

        for turn_set in num_turns_until_algorithm:
            human_move = str(random.choice(processor.get_valid_moves()))
            processor.execute_move(human_move, player_1.token)
            actuals.append(self.benchmark(strat.execute))
        board.spaces = [None] * 9

        for index, actual in enumerate(actuals):
            self.assertGreaterEqual(expected, actual,
                                    msg=f"Failed on turn number {index + 1}")

    def benchmark(self, method):
        start_time = time.time()
        method()
        return time.time() - start_time

