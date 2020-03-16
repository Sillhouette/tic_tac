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

class ThreeByThreeHardStrategySmokeTest(unittest.TestCase):
    def test_computer_makes_instantaneous_moves_smoke_test(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        player_1 = HumanPlayer(Mock(), Mock())
        player_2 = ComputerPlayer(processor, Mock())
        players = [player_1, player_2]
        processor.set_players(players)
        strat = ThreeByThreeHardStrategy(processor, player_2)
        turns_until_algorithm = 2
        num_turns = range(turns_until_algorithm)
        num_times_ran = range(10)
        expected = 0.5
        actuals = []

        for run in num_times_ran:
            for turn_set in num_turns:
                human_move = str(random.choice(processor.get_valid_moves()))
                processor.execute_move(human_move, player_1.token)
                actuals.append(self.benchmark(strat.execute))
            board.spaces = [None] * 9

        for index, actual in enumerate(actuals):
            self.assertGreaterEqual(expected, actual,
                                    msg=f"Failed on turn number {(index + 1) / 2}")

    def benchmark(self, method):
        start_time = time.time()
        method()
        return time.time() - start_time

