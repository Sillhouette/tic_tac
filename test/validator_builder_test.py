import unittest
import src.constants as constants

from src.validator_builder import ValidatorBuilder
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor

class ValidatorBuilderTest(unittest.TestCase):
    def test_build_validator_can_build_3x3_board(self):
        builder = ValidatorBuilder()
        board = ThreeByThreeBoard()
        expected = ThreeByThreeProcessor(board)

        validator = builder.build_validator(expected)
        actual = validator.processor

        self.assertEqual(expected, actual)
