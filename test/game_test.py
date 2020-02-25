import unittest

from unittest.mock import Mock, patch
from src.game import Game

class GameTest(unittest.TestCase):
    @patch.object(Game, 'play')
    def test_start(self, play):
        cli = Mock()
        player_1, player_2 = Mock(), Mock()
        board = Mock()
        game = Game(cli, board, [player_1, player_2])

        game.start()

        cli.welcome.assert_called()
        game.play.assert_called()

    @patch.object(Game, 'turn')
    @patch.object(Game, 'game_is_over')
    def test_play(self, turn, game_is_over):
        cli = Mock()
        player_1, player_2 = Mock(), Mock()
        board = Mock()

        game = Game(cli, board, [player_1, player_2])
        game.game_is_over.side_effect = [False, True]

        game.play()

        cli.display_board.assert_called()
        game.game_is_over.assert_called()
        game.turn.assert_called()

    def test_input_to_index(self):
        game = Game()
        expected = 0

        actual = game.input_to_index("1")

        self.assertEqual(expected, actual)

    def test_input_to_index_2(self):
        game = Game()
        expected = 5

        actual = game.input_to_index("6")

        self.assertEqual(expected, actual)

    def test_current_player(self):
        game = Game()
        expected = game.players[0]

        actual = game.current_player()

        self.assertEqual(expected, actual)

    def test_current_player_2(self):
        game = Game()
        game.board.spaces[0] = "X"
        expected = game.players[1]

        actual = game.current_player()

        self.assertEqual(expected, actual)

    def test_game_is_over(self):
        cli = Mock()
        game = Game(cli=cli)

        game.board.spaces = ["X"] * 9
        expected = True

        actual = game.game_is_over()

        self.assertEqual(expected, actual)

    def test_game_is_over_2(self):
        cli = Mock()
        game = Game(cli=cli)
        game.exit = True
        expected = True

        actual = game.game_is_over()

        self.assertEqual(expected, actual)

    def test_game_is_not_over(self):
        game = Game()
        expected = False

        actual = game.game_is_over()

        self.assertEqual(expected, actual)
