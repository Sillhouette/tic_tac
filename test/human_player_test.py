import unittest

from unittest.mock import Mock

from src.human_player import HumanPlayer as Player

class HumanPlayerTest(unittest.TestCase):
    def test_player_name(self):
        name = "Chuck Norris" 
        cli = Mock()
        validator = Mock()

        player = Player(cli, validator, name)

        self.assertEqual(player.name, name)
    
    def test_default_player_token(self):
        name = "Chuck Norris"
        token = "X"
        validator = Mock()
        cli = Mock()

        player = Player(cli, validator, name)

        self.assertEqual(player.token, token)

    def test_setting_player_token(self):
        name = "Chuck Norris"
        token = "¤"
        validator = Mock()
        cli = Mock()
        player = Player(cli, validator, name)

        player.set_token(token)

        self.assertEqual(player.token, token)

