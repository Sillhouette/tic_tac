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
        move = "6"
        token = "O"
        expected = [None, None, None, None, None, "O", None, None, None]

        board.update(move, token)
        actual = board.spaces

        self.assertEqual(expected, actual)
        
    def test_update_board_places_different_token_correctly(self):
        board = ThreeByThreeBoard()
        move = "2"
        token = "X"
        expected = [None, "X", None, None, None, None, None, None, None]

        board.update(move, token)
        actual = board.spaces

        self.assertEqual(expected, actual)

    def test_turn_count_returns_correctly_when_one_turn_made(self):
        board = ThreeByThreeBoard()
        expected = 1

        board.update("1", "X")
        
        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_turn_count_returns_correctly_when_four_turns_made(self):
        board = ThreeByThreeBoard()
        expected = 4

        board.update("1", "X")
        board.update("2", "O")
        board.update("5", "X")
        board.update("9", "O")
        actual = board.turn_count()

        self.assertEqual(expected, actual)

    def test_move_to_index_returns_4_when_given_5(self):
        board = ThreeByThreeBoard()
        move = "5"
        expected = 4

        actual = board.move_to_index(move)

        self.assertEqual(expected, actual)

    def test_move_to_index_returns_8_when_given_9(self):
        board = ThreeByThreeBoard()
        move = "9"
        expected = 8

        actual = board.move_to_index(move)

        self.assertEqual(expected, actual)

    def test_move_result_returns_none_when_game_not_over(self):
        board = ThreeByThreeBoard()
        move = "5"
        token = "X"
        expected_return = None
        expected_board =  [None, None, None, None, "X", None, None, None, None]

        actual_return = board.move_result(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)

    def test_move_result_returns_winning_token_when_winner(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "X", "O", "O", None, "X", "X", None, "X"]
        move = "8"
        token = "X"
        expected_return = "X"
        expected_board = ["X", "X", "O", "O", None, "X", "X", "X", "X"]

        actual_return = board.move_result(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)

    def test_move_result_returns_CATS_when_board_full(self):
        board = ThreeByThreeBoard()
        board.spaces = ["X", "X", "O", "O", "O", "X", "X", None, "X"]
        move = "8"
        token = "O"
        expected_return = "finished"
        expected_board = ["X", "X", "O", "O", "O", "X", "X", "O", "X"]

        actual_return = board.move_result(move, token)
        actual_board = board.spaces

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_board, actual_board)

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

    def test_valid_move_returns_true_when_valid(self):
        board = ThreeByThreeBoard()
        move = "1"
        expected = True

        actual = board.valid_move(move)

        self.assertEqual(expected, actual)

    def test_valid_move_returns_false_when_out_of_bounds(self):
        board = ThreeByThreeBoard()
        move = "55"
        expected = False

        actual = board.valid_move(move)

        self.assertEqual(expected, actual)

    def test_valid_move_returns_false_when_already_taken(self):
        board = ThreeByThreeBoard()
        position = 2
        board.spaces[position] = "X"
        move = "3"
        expected = False

        actual = board.valid_move(move)

        self.assertEqual(expected, actual)

    def test_winner_returns_winning_token_when_player_has_won(self):
        board = ThreeByThreeBoard()
        token = "X"
        expected = token

        board.update("1", token)
        board.update("2", token)
        board.update("3", token)
        actual = board.winner()

        self.assertEqual(expected, actual)

    def test_winner_returns_None_when_no_winner_exists(self):
        board = ThreeByThreeBoard()
        token_1 = "X"
        token_2 = "O"
        X_moves = ["1", "2", "6", "7","9"]
        O_moves = ["3", "4", "5", "8"]
        expected = None

        for move in X_moves:
            board.update(move, token_1)

        for move in O_moves:
            board.update(move, token_2)

        actual = board.winner()

        self.assertEqual(expected, actual)
