import math

import src.constants as constants

from src.minimax import Minimax

class ThreeByThreeHardStrategy():
    SECOND_MOVE = {
        0: "5",
        1: "1",
        2: "5",
        3: "1",
        4: "1",
        5: "3",
        6: "5",
        7: "2",
        8: "5"
    }

    def __init__(self, processor, computer_player):
        self.processor = processor
        self.computer_player = computer_player
        self.minimax = None

    def set_minimax(self):
        self.minimax = Minimax(self.processor, self.computer_player.get_index())

    def execute(self):
        turn = self.processor.board.turn_count()
        if turn == 0:
            return [constants.MOVE, "1"]
        if turn == 1:
            first_taken = self.processor.get_taken_positions()[0]
            return [constants.MOVE, self.SECOND_MOVE[first_taken]]

        if not self.minimax: self.set_minimax()
        return self.get_best_move()

    def get_best_move(self):
        next_player_index = self.processor.next_player_index(self.computer_player.get_index())
        valid_moves = self.processor.get_valid_moves()
        best_score = -math.inf
        best_move = None
        for move in valid_moves:
            score = self.minimax.execute(move, 0, self.computer_player.token,
                                    next_player_index)
            if score > best_score:
                best_score = score
                best_move = move

        return [constants.MOVE, str(best_move)]

