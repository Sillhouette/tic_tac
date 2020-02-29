import unittest
import src.constants as constants

from src.validator_builder import ValidatorBuilder

class ValidatorBuilderTest(unittest.TestCase):
    def test_build_validator_3x3(self):
        builder = ValidatorBuilder()
        validator_type = constants.THREE_BY_THREE
        expected = validator_type

        validator = builder.build_validator(validator_type)
        actual = validator.type

        self.assertEqual(expected, actual)
