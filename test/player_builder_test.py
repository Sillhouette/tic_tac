import unittest

from unittest.mock import Mock
from src.player_builder import PlayerBuilder
from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer

class PlayerBuilderTest(unittest.TestCase):

    def test_build_players_builds_list_of_two_players(self):
        validator = Mock()
        board = Mock()
        cli = Mock()
        builder = PlayerBuilder(validator, board, cli)
        tokens = ['X', 'O']
        expected = True
        expected_size = 2

        players = builder.build_players(tokens)
        actual = all(isinstance(player, (HumanPlayer, ComputerPlayer)) for player in players)
        actual_size = len(players)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_size, actual_size)



