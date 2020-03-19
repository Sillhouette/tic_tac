import random
import time
import math

import src.constants as constants
from src.strategy_builder import StrategyBuilder

class ComputerPlayer():
    def __init__(self, processor, cli, token="O", difficulty=constants.HARD, data_gatherer=None):
        self.token = token
        self.processor = processor
        self.cli = cli
        self.set_strategy(difficulty)
        self.data_gatherer = data_gatherer
        
    def set_token(self, token):
        self.token = token

    def set_strategy(self, difficulty):
        strategy_builder = StrategyBuilder(self.processor, self)
        self.strategy = strategy_builder.build(difficulty)

    def get_index(self):
        return self.processor.players.index(self)

    def get_move(self):
        self.cli.notify_for_computer_turn()
        recording = False
        if self.data_gatherer:
            recording = True
        return self.strategy.execute(recording)

