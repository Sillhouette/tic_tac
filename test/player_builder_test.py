import unittest

import src.constants as constants

from unittest.mock import Mock
from src.player_builder import PlayerBuilder
from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer
from src.three_by_three_validator import ThreeByThreeValidator
from src.cli import Cli

class PlayerBuilderTest(unittest.TestCase):

    def test_build_players_builds_list_of_two_human_players(self):
        validator = Mock(ThreeByThreeValidator)
        processor = Mock()
        cli = Mock()
        builder = PlayerBuilder(validator, processor, cli)
        validator.get_valid_player_choice.return_value = "1"
        tokens = ['X', 'O']
        expected = True
        expected_size = 2

        players = builder.build_players(tokens)
        actual = all(isinstance(player, HumanPlayer) for player in players)
        actual_size = len(players)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_size, actual_size)

    def test_build_players_builds_list_of_one_human_one_computer(self):
        validator = Mock(ThreeByThreeValidator)
        processor = Mock()
        cli = Mock()
        builder = PlayerBuilder(validator, processor, cli)
        validator.get_valid_player_choice.return_value = "2"
        tokens = ['X', 'O']
        expected = True
        expected_size = 2

        players = builder.build_players(tokens)
        player_1 = isinstance(players[0], HumanPlayer)
        player_2 = isinstance(players[1], ComputerPlayer)
        actual = all([player_1, player_2])
        actual_size = len(players)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_size, actual_size)

    def test_build_players_builds_list_of_human_and_computer(self):
        validator = Mock(ThreeByThreeValidator)
        processor = Mock()
        cli = Mock()
        builder = PlayerBuilder(validator, processor, cli)
        validator.get_valid_player_choice.return_value = "3"
        tokens = ['X', 'O']
        expected = True
        expected_size = 2

        players = builder.build_players(tokens)
        player_1 = isinstance(players[0], HumanPlayer)
        player_2 = isinstance(players[1], ComputerPlayer)
        actual = all([player_1, player_2])
        actual_size = len(players)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_size, actual_size)

    def test_build_players_returns_exit_when_chosen(self):
        validator = Mock()
        processor = Mock()
        cli = Mock()
        builder = PlayerBuilder(validator, processor, cli)
        builder.get_valid_choice = Mock()
        builder.get_valid_choice.return_value = constants.EXIT
        tokens = ['X', 'O']
        expected = constants.EXIT

        actual = builder.build_players(tokens)

        self.assertEqual(expected, actual)

