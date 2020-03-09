import src.constants as constants

from src.three_by_three_validator import ThreeByThreeValidator

class ValidatorBuilder():
    def build_validator(self, processor):
       return ThreeByThreeValidator(processor)
