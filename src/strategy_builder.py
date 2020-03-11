import src.constants as constants

from src.three_by_three_hard_strategy import ThreeByThreeHardStrategy
from src.three_by_three_easy_strategy import ThreeByThreeEasyStrategy

class StrategyBuilder():
    def __init__(self, processor, computer_player):
        self.processor = processor
        self.computer_player = computer_player

    def build(self, difficulty):
        board_type = self.processor.board.type
        if board_type == constants.THREE_BY_THREE:
            if difficulty == constants.HARD:
                return ThreeByThreeHardStrategy(self.processor, self.computer_player)
            elif difficulty == constants.EASY:
                return ThreeByThreeEasyStrategy(self.processor, self.computer_player)
