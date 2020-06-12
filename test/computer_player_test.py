import unittest

import src.constants as constants

from unittest.mock import Mock
from src.computer_player import ComputerPlayer

class ComputerPlayerTest(unittest.TestCase):
    def test_setting_computer_player_token(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        cli = Mock()
        computer = ComputerPlayer(processor, cli)
        token = "%"
        expected = token

        computer.set_token(token)
        actual = computer.token

        self.assertEqual(expected, actual)

    def test_get_index_returns_index_of_computer_player(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        cli = Mock()
        computer = ComputerPlayer(processor, cli)
        processor.players = [computer]
        expected = 0

        actual = computer.get_index()

        self.assertEqual(expected, actual)

    def test_get_index_returns_index_of_computer_player_2(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        cli = Mock()
        computer = ComputerPlayer(processor, cli)
        human = Mock()
        processor.players = [human, computer]
        expected = 1

        actual = computer.get_index()

        self.assertEqual(expected, actual)

    def test_get_move_invokes_strategy_execute(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        cli = Mock()
        computer = ComputerPlayer(processor, cli)
        computer.strategy = Mock()
        computer.strategy.execute = Mock()

        computer.get_move()

        computer.strategy.execute.assert_called()

