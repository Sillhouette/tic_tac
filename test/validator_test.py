import unittest

from src.validator import Validator
from src.three_by_three_board import ThreeByThreeBoard

class ValidatorTest(unittest.TestCase):
    def test_validate_move_3x3(self):
        move = "1"
        board_type = "3x3"
        board = ThreeByThreeBoard()
        validator = Validator()
        expected = ["move", "1"]

        actual = validator.validate_move(move, board)

        self.assertEqual(expected, actual)
    
    def test_within_board(self):
        board = ThreeByThreeBoard()
        validator = Validator()
        position = 0
        expected = True

        actual = validator.within_board(position, board)

        self.assertEqual(expected, actual)
 
    def test_within_board_2(self):
        board = ThreeByThreeBoard()
        validator = Validator()
        position = 9
        expected = True

        actual = validator.within_board(position, board)

        self.assertEqual(expected, actual)


    def test_not_within_board(self):
        board = ThreeByThreeBoard()
        validator = Validator()
        position = 55
        expected = False

        actual = validator.within_board(position, board)

        self.assertEqual(expected, actual)

    def test_position_not_taken(self):
        board = ThreeByThreeBoard()
        validator = Validator()
        position = 0
        expected = False

        actual = validator.position_taken(position, board)

        self.assertEqual(expected, actual)

    def test_position_taken(self):
        board = ThreeByThreeBoard()
        position = 0
        board.spaces[position] = "X"
        validator = Validator()
        expected = True

        actual = validator.position_taken(position, board)

        self.assertEqual(expected, actual)

    def validate_3x3_move(self):
        board = ThreeByThreeBoard()
        move = "1"
        validator = Validator()
        expected = True

        actual = validator.validate_3x3_move(move, board)

        self.assertEqual(expected, actual)

    def validate_3x3_move_out_of_bounds(self):
        board = ThreeByThreeBoard()
        move = "55"
        validator = Validator()
        expected = False

        actual = validator.validate_3x3_move(move, board)

        self.assertEqual(expected, actual)

    def validate_3x3_move_taken(self):
        board = ThreeByThreeBoard()
        position = 2
        board.spaces[position] = "X"
        validator = Validator()
        move = "3"
        expected = False

        actual = validator.test_validate_move_3x3(move, board)

        self.assertEqual(expected, actual)
        
    def test_validate_3x3(self):
        board = ThreeByThreeBoard()
        move = "5"
        validator = Validator()
        expected = ["move", "5"]

        actual = validator.validate_3x3(move, board)

        self.assertEqual(expected, actual)

    def test_validate_3x3_invalid(self):
        board = ThreeByThreeBoard()
        move = "87"
        validator = Validator()
        expected = ["invalid", "87"]

        actual = validator.validate_3x3(move, board)

        self.assertEqual(expected, actual)
