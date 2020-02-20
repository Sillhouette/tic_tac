import unittest

from src.game import Game

# I'm not sure how to unit test init, start, play, and turn
# Should I just write integration tests for them?

class GameTest(unittest.TestCase):
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
        expected = game.player_1

        actual = game.current_player()

        self.assertEqual(expected, actual)

    def test_current_player_2(self):
        game = Game()
        game.board.spaces[0] = "X"
        expected = game.player_2

        actual = game.current_player()

        self.assertEqual(expected, actual)
