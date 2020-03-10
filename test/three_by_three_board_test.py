import unittest

from src.three_by_three_board import ThreeByThreeBoard

class ThreeByThreeBoardTest(unittest.TestCase):
    def test_full_board(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "O", "X", "O", "O", "X", "O", "O", "X"]
        expected = True

        actual = board.full()

        self.assertEqual(expected, actual)

    def test_not_full_board(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "O", None, "O", "X", None, None, "O", "X"]
        expected = False

        actual = board.full()

        self.assertEqual(expected, actual)

    def test_update_board_places_token_correctly(self):
        board = ThreeByThreeBoard()
        index = 5
        token = "O"
        expected = [None, None, None, None, None, "O", None, None, None]

        board.update(index, token)
        actual = board.spaces

        self.assertEqual(expected, actual)
        
    def test_update_board_places_different_token_correctly(self):
        board = ThreeByThreeBoard()
        index = 1
        token = "X"
        expected = [None, "X", None, None, None, None, None, None, None]

        board.update(index, token)
        actual = board.spaces

        self.assertEqual(expected, actual)

    def test_turn_count_returns_correctly_when_one_turn_made(self):
        board = ThreeByThreeBoard()
        index = 1
        token = "X"
        expected = 1

        board.update(index, token)
        
        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_turn_count_returns_correctly_when_four_turns_made(self):
        board = ThreeByThreeBoard()
        expected = 4

        board.update(1, "X")
        board.update(2, "O")
        board.update(5, "X")
        board.update(8, "O")
        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_within_board_returns_true_when_within_board(self):
        board = ThreeByThreeBoard()
        position = 0
        expected = True

        actual = board.within_board(position)

        self.assertEqual(expected, actual)

    def test_within_board_returns_true_when_given_9(self):
        board = ThreeByThreeBoard()
        position = 9
        expected = True

        actual = board.within_board(position)

        self.assertEqual(expected, actual)

    def test_within_board_returns_false_when_not_within_board(self):
        board = ThreeByThreeBoard()
        position = 55
        expected = False

        actual = board.within_board(position)

        self.assertEqual(expected, actual)

    def test_position_taken_retuns_false_when_not_taken(self):
        board = ThreeByThreeBoard()
        position = 0
        expected = False

        actual = board.position_taken(position)

        self.assertEqual(expected, actual)

    def test_position_taken_returns_true_when_taken(self):
        board = ThreeByThreeBoard()
        position = 0
        board.spaces[position] = "X"
        expected = True

        actual = board.position_taken(position)

        self.assertEqual(expected, actual)
