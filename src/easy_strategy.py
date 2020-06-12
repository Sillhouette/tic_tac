import random

import src.constants as constants

class EasyStrategy():
    def __init__(self, processor, computer_player):
        self.processor = processor
        self.computer_player = computer_player

    def execute(self, recording=False):
        return self.get_random_move()

    def get_random_move(self):
        choice = random.choice(self.processor.get_valid_moves())

        return [constants.MOVE, str(choice)]

