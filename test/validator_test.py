import unittest
import src.constants as constants

from unittest.mock import Mock
from src.validator import Validator
from src.board import Board
from src.processor import Processor
from src.cli import Cli

class ValidatorTest(unittest.TestCase):
    def test_validate_returns_proper_action_when_move_is_valid(self):
        move = "1"
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        validator = Validator()
        validator.set_processor(processor)
        expected = ["move", "1"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_returns_error_action_when_move_not_valid(self):
        board = Board(constants.THREE_BY_THREE)
        move = "Gibberish"
        processor = Processor(board)
        validator = Validator()
        validator.set_processor(processor)
        expected = ["error", "gibberish"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_returns_error_action_when_move_out_of_bounds(self):
        board = Board(constants.THREE_BY_THREE)
        move = "87"
        processor = Processor(board)
        validator = Validator()
        validator.set_processor(processor)
        expected = ["error", "87"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

