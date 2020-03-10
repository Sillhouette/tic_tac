import unittest
import src.constants as constants

from unittest.mock import Mock, patch
from src.game import Game
from src.app import App
from src.human_player import HumanPlayer as Player
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_validator import ThreeByThreeValidator

class AppTest(unittest.TestCase):
    @patch.object(Game, "play")
    def test_initialize_welcomes_player(self, game_play):
        cli = Mock()
        app = App(cli)
        app.setup_players = Mock()
        
        actual = app.initialize()

        cli.welcome.assert_called()
   
    @patch.object(Game, "play")
    def test_initialize_sets_players(self, game_play):
        cli = Mock()
        cli.get_player_tokens = Mock()
        cli.get_player_tokens.return_value = ["X", "O"]
        board = Mock()
        validator = Mock()
        game = Mock()
        app = App(cli, board, validator, game=game)
        app.setup_players = Mock()
        
        actual = app.initialize()

        app.setup_players.assert_called()
   
    @patch.object(Game, "play")
    def test_initialize_sets_board(self, play):
        cli = Mock()
        cli.set_presenter_type = Mock()
        cli.get_player_tokens = Mock()
        cli.get_player_token.return_values = ["X", "O"]
        app = App(cli)
        app.setup_players = Mock()
        app.setup_board = Mock()
        app.board = Mock()
        app.board.type = constants.THREE_BY_THREE

        actual = app.initialize()

        app.setup_board.assert_called()
    
    @patch.object(Game, "play")
    def test_initialize_sets_validator(self, game_play):
        cli = Mock()
        app = App(cli)
        app.setup_players = Mock()
        app.setup_validator = Mock()

        actual = app.initialize()

        app.setup_validator.assert_called()
    
    @patch.object(Game, "__init__", lambda a, b, c, d, e, f: None)
    @patch.object(Game, "play")
    def test_initialize_starts_game(self, game_play):
        cli = Mock()
        app = App(cli)
        app.setup_players = Mock()

        actual = app.initialize()

        app.game.play.assert_called()

    def test_setup_players_can_setup_players(self):
        cli = Mock()
        cli.get_player_tokens = Mock()
        cli.get_board_type = Mock()
        cli.get_player_tokens.return_value = ["X", "O"]
        cli.get_board_type.return_value = constants.THREE_BY_THREE
        app = App(cli)
        app.setup_board()
        app.setup_processor()
        app.setup_validator()
        expected_length = 2
        expected_is_players = True

        app.setup_players()
        actual = app.players
        actual_length = len(actual)
        actual_is_players = any(isinstance(player, Player) for player in actual)

        self.assertEqual(expected_length, actual_length)
        self.assertEqual(expected_is_players, actual_is_players)

    def test_setup_board_can_setup_3x3_board(self):
        cli = Mock()
        cli.get_board_type = Mock()
        cli.get_board_type.return_value = "3x3"
        app = App(cli)
        expected = True

        app.setup_board()
        board = app.board

        actual = isinstance(board, ThreeByThreeBoard)

        self.assertEqual(expected, actual)

    def test_setup_validator_can_setup_3x3_validator(self):
        cli = Mock()
        board = Mock()
        board.type = "3x3"
        app = App(cli)
        expected = True

        app.setup_validator()
        validator = app.validator
        actual = isinstance(validator, ThreeByThreeValidator)

        self.assertEqual(expected, actual)

