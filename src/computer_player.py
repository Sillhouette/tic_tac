import random
import src.constants as constants
import time
import math

from src.minimax import Minimax

class ComputerPlayer():
    def __init__(self, processor, cli, token="O", difficulty="hard"):
        self.token = token
        self.processor = processor
        self.cli = cli
        self.minimax = Minimax(processor, self.token)
        self.difficulty = difficulty
        
    def set_token(self, token):
        self.token = token

    def get_move(self):
        if self.difficulty == "hard":
            return self.get_best_move()
        else:
            return self.get_random_move()

    def get_best_move(self):
        start_time = time.time()
        self.cli.notify_for_computer_turn()
        valid_moves = self.processor.get_valid_moves()
        best_score = -math.inf
        best_move = None
        for move in valid_moves:
            self.processor.execute_move(move, self.token)
            score = self.minimax.execute(0, False)
            self.processor.execute_move(move, None)
            if score > best_score:
                best_score = score
                best_move = move

        print("Computer took:", time.time() - start_time, "to make a move")
        return [constants.MOVE, str(best_move)]

    def get_random_move(self):
        self.cli.notify_for_computer_turn()

        choice = random.choice(self.processor.get_valid_moves())

        return [constants.MOVE, str(choice)]

