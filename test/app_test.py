import unittest

from unittest.mock import Mock, patch
from src.game import Game
from src.app import App
from src.player import Player
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_validator import ThreeByThreeValidator

class AppTest(unittest.TestCase):
    @patch.object(Game, "play")
    def test_initialize_welcomes_player(self, game_play):
        cli = Mock()
        app = App(cli)
        app.setup_players = Mock()
        
        expected = app.initialize()

        cli.welcome.assert_called()
   
    @patch.object(Game, "play")
    def test_initialize_sets_players(self, game_play):
        cli = Mock()
        app = App(cli)
        app.setup_players = Mock()
        
        expected = app.initialize()

        app.setup_players.assert_called()
   
    @patch.object(Game, "play")
    def test_initialize_sets_board(self, game_play):
        cli = Mock()
        app = App(cli)
        app.setup_players = Mock()
        app.setup_board = Mock()

        expected = app.initialize()

        app.setup_board.assert_called()
    
    @patch.object(Game, "play")
    def test_initialize_sets_validator(self, game_play):
        cli = Mock()
        app = App(cli)
        app.setup_players = Mock()
        app.setup_validator = Mock()

        expected = app.initialize()

        app.setup_validator.assert_called()
    
    @patch.object(Game, "__init__", lambda a, b, c, d, e: None)
    @patch.object(Game, "play")
    def test_initialize_starts_game(self, game_play):
        cli = Mock()
        app = App(cli)
        app.setup_players = Mock()

        expected = app.initialize()

        app.game.play.assert_called()


    def test_setup_players(self):
        cli = Mock()
        cli.get_player_tokens = Mock()
        cli.get_player_tokens.return_value = ["X", "O"]
        app = App(cli)
        expected_length = 2
        expected_is_players = True

        actual = app.setup_players()
        actual_length = len(actual)
        actual_is_players = any(isinstance(player, Player) for player in actual)

        self.assertEqual(expected_length, actual_length)
        self.assertEqual(expected_is_players, actual_is_players)

    def test_setup_3x3_board(self):
        cli = Mock()
        cli.get_board_type = Mock()
        cli.get_board_type.return_value = "3x3"
        app = App(cli)
        expected = True

        board = app.setup_board()
        actual = isinstance(board, ThreeByThreeBoard)

        self.assertEqual(expected, actual)

    def test_setup_validator(self):
        cli = Mock()
        board = Mock()
        board.type = "3x3"
        app = App(cli)
        expected = True

        validator = app.setup_validator(board)
        actual = isinstance(validator, ThreeByThreeValidator)

        self.assertEqual(expected, actual)
