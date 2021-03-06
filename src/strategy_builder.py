import src.constants as constants

from src.hard_strategy import HardStrategy
from src.easy_strategy import EasyStrategy

class StrategyBuilder():
    def __init__(self, processor, computer_player):
        self.processor = processor
        self.computer_player = computer_player

    def build(self, difficulty):
        if difficulty == constants.HARD:
            return HardStrategy(self.processor, self.computer_player)
        elif difficulty == constants.EASY:
            return EasyStrategy(self.processor, self.computer_player)
