import unittest

from src.player_builder import PlayerBuilder
from src.player import Player

class PlayerBuilderTest(unittest.TestCase):

    def test_build_players_builds_list_of_two_players(self):
        builder = PlayerBuilder()
        tokens = ['X', 'O']
        expected = True
        expected_size = 2

        players = builder.build_players(tokens)
        actual = all(isinstance(player, Player) for player in players)
        actual_size = len(players)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_size, actual_size)



