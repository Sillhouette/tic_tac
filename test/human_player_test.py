import unittest
import src.constants as constants

from unittest.mock import Mock

from src.human_player import HumanPlayer as Player
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_validator import ThreeByThreeValidator

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

    def test_get_move_returns_only_valid_moves(self):
        cli = Mock()
        board = ThreeByThreeBoard()
        validator = ThreeByThreeValidator(board)
        cli.request_move = Mock()
        moves = ["1", "55", "exit", "gibberish"]
        cli.request_move.side_effect = moves 
        player = Player(cli, validator)
        expected_list = [
            [constants.MOVE, moves[0]],
            [constants.ERROR, moves[1]],
            [constants.EXIT, None],
            [constants.ERROR, moves[3]]
        ]

        actual_list = [
            player.get_move(),
            player.get_move(),
            player.get_move(),
            player.get_move()
        ]
        self.assertListEqual(expected_list, actual_list)

    def test_validate_move_properly_validates_various_choices(self):
        cli = Mock()
        board = ThreeByThreeBoard()
        validator = ThreeByThreeValidator(board)
        player = Player(cli, validator)
        moves = ["9", "357", "exit", "chuck norris wins"]
        expected_list = [
            [constants.MOVE, moves[0]],
            [constants.ERROR, moves[1]],
            [constants.EXIT, None],
            [constants.ERROR, moves[3]]
        ]

        actual_list = []
        for move in moves:
            actual_list.append(player.validate_move(move))

        self.assertListEqual(expected_list, actual_list)
