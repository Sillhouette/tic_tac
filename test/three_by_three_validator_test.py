import unittest

from src.three_by_three_validator import ThreeByThreeValidator as Validator
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor

class ThreeByThreeValidatorTest(unittest.TestCase):
    def test_validate_returns_proper_action_when_move_is_valid(self):
        move = "1"
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        validator = Validator(processor)
        expected = ["move", "1"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_returns_error_action_when_move_not_valid(self):
        board = ThreeByThreeBoard()
        move = "Gibberish"
        processor = ThreeByThreeProcessor(board)
        validator = Validator(processor)
        expected = ["error", "gibberish"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_returns_error_action_when_move_out_of_bounds(self):
        board = ThreeByThreeBoard()
        move = "87"
        processor = ThreeByThreeProcessor(board)
        validator = Validator(processor)
        expected = ["error", "87"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_input_returns_false_when_not_valid(self):
        board = ThreeByThreeBoard()
        move = "gibberish"
        processor = ThreeByThreeProcessor(board)
        validator = Validator(processor)
        expected = False

        actual = validator.validate_input(move)

        self.assertEqual(expected, actual)

    def test_validate_input_returns_true_when_valid(self):
        board = ThreeByThreeBoard()
        move = "6"
        processor = ThreeByThreeProcessor(board)
        validator = Validator(processor)
        expected = True

        actual = validator.validate_input(move)

        self.assertEqual(expected, actual)
        
