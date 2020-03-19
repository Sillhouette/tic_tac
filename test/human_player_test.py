import unittest
import src.constants as constants

from unittest.mock import Mock

from src.human_player import HumanPlayer as Player
from src.board import Board
from src.processor import Processor

class HumanPlayerTest(unittest.TestCase):
    def test_player_name(self):
        name = "Chuck Norris" 
        cli = Mock()

        player = Player(cli, name)

        self.assertEqual(player.name, name)
    
    def test_default_player_token(self):
        name = "Chuck Norris"
        token = "X"
        cli = Mock()

        player = Player(cli, name)

        self.assertEqual(player.token, token)

    def test_setting_player_token(self):
        name = "Chuck Norris"
        token = "¤"
        cli = Mock()
        player = Player(cli, name)

        player.set_token(token)

        self.assertEqual(player.token, token)

    @unittest.skip("Outdated Test")
    def test_get_move_returns_only_valid_moves(self):
        cli = Mock()
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        cli.request_move = Mock()
        moves = ["1", "55", "exit", "gibberish"]
        cli.request_move.side_effect = moves 
        player = Player(cli)
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

    @unittest.skip("Outdated Test")
    def test_get_move_properly_returns_based_on_input(self):
        cli = Mock()
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        player = Player(cli)
        moves = ["9", "357", "exit", "chuck norris wins"]
        expected_list = [
            [constants.MOVE, moves[0]],
            [constants.ERROR, moves[1]],
            [constants.EXIT, None],
            [constants.ERROR, moves[3]]
        ]

        actual_list = []
        for move in moves:
            actual_list.append(player.get_move())

        self.assertListEqual(expected_list, actual_list)

