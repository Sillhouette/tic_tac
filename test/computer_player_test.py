import unittest

from unittest.mock import Mock
from src.computer_player import ComputerPlayer
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor

class ComputerPlayerTest(unittest.TestCase):
    def test_setting_computer_player_token(self):
        processor = Mock()
        cli = Mock()
        computer = ComputerPlayer(processor, cli)
        token = "%"
        expected = token

        computer.set_token(token)
        actual = computer.token

        self.assertEqual(expected, actual)

    def test_get_index_returns_index_of_computer_player(self):
        processor = Mock()
        cli = Mock()
        computer = ComputerPlayer(processor, cli)
        processor.players = [computer]
        expected = 0

        actual = computer.get_index()

        self.assertEqual(expected, actual)

    def test_get_index_returns_index_of_computer_player_2(self):
        processor = Mock()
        cli = Mock()
        computer = ComputerPlayer(processor, cli)
        human = Mock()
        processor.players = [human, computer]
        expected = 1

        actual = computer.get_index()

        self.assertEqual(expected, actual)

    def test_get_move_invokes_strategy_execute(self):
        processor = Mock()
        cli = Mock()
        computer = ComputerPlayer(processor, cli)
        computer.strategy = Mock()
        computer.strategy.execute = Mock()

        computer.get_move()

        computer.strategy.execute.assert_called()
