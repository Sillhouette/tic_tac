import unittest

import src.constants as constants

from unittest.mock import Mock
from src.player_builder import PlayerBuilder
from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer
from src.validator import Validator
from src.cli import Cli

class PlayerBuilderTest(unittest.TestCase):

    def test_build_players_builds_list_of_two_human_players(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        cli = Mock()
        builder = PlayerBuilder(processor, cli)
        choice = "1"
        tokens = ['X', 'O']
        expected = True
        expected_size = 2

        players = builder.build_players(tokens, choice)
        actual = all(isinstance(player, HumanPlayer) for player in players)
        actual_size = len(players)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_size, actual_size)

    def test_build_players_builds_list_of_one_human_one_computer(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        cli = Mock()
        builder = PlayerBuilder(processor, cli)
        choice = "2"
        tokens = ['X', 'O']
        expected = True
        expected_size = 2

        players = builder.build_players(tokens, choice)
        player_1 = isinstance(players[0], HumanPlayer)
        player_2 = isinstance(players[1], ComputerPlayer)
        actual = all([player_1, player_2])
        actual_size = len(players)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_size, actual_size)

    def test_build_players_builds_list_of_human_and_computer(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        cli = Mock()
        builder = PlayerBuilder(processor, cli)
        choice = "3"
        tokens = ['X', 'O']
        expected = True
        expected_size = 2

        players = builder.build_players(tokens, choice)
        player_1 = isinstance(players[0], HumanPlayer)
        player_2 = isinstance(players[1], ComputerPlayer)
        actual = all([player_1, player_2])
        actual_size = len(players)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_size, actual_size)

