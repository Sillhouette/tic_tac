import unittest

from src.player import Player

class PlayerTest(unittest.TestCase):
    def test_player_name(self):
        name = "Chuck Norris" 

        player = Player(name)

        self.assertEqual(player.name, name)
    
    def test_default_player_token(self):
        name = "Chuck Norris"
        token = "X"

        player = Player(name)

        self.assertEqual(player.token, token)

    def test_setting_player_token(self):
        name = "Chuck Norris"
        token = "¤"
        player = Player(name)

        player.set_token(token)

        self.assertEqual(player.token, token)

