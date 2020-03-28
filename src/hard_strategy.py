import math
import json
import pdb

import src.constants as constants

from src.minimax import Minimax
from src.data_gatherer import DataGatherer

class HardStrategy():

    def __init__(self, processor, computer_player):
        self.processor = processor
        self.computer_player = computer_player
        self.minimax = None
        self.optimal_moves = None

    def set_minimax(self):
        data_gatherer = DataGatherer()
        self.minimax = Minimax(self.processor,
                               self.computer_player.get_index(), max_depth=4, data_gatherer=data_gatherer)

    def load_optimal_moves(self):
        optimal_moves = None
        board_type = self.processor.board.type
        with open(f'{board_type}_optimal_moves.json', 'r') as openfile:
            optimal_moves = json.load(openfile)

        self.optimal_moves = optimal_moves

    def execute(self):
        return self.get_best_move()

    def get_best_move(self):
        self.load_resources()

        if "14" in self.processor.get_valid_moves():
            return [constants.MOVE, "14"]
        
        optimal_key = self.stringify_board_state()
        if optimal_key in self.optimal_moves:
            best_move = self.optimal_moves[self.stringify_board_state()]
        else:
            best_move = self.minimax.get_best_move(0, self.computer_player.get_index())
        
        return [constants.MOVE, best_move]

    def stringify_board_state(self):
        board_state = self.processor.board.spaces
        scrubbed_board = self.scrub_state(board_state)
        return "".join(scrubbed_board)

    def scrub_state(self, board_state):
        return ["_" if token is None else token for token in board_state]
    
    def load_resources(self):
        if not self.minimax:
            self.set_minimax()
        if not self.optimal_moves:
            self.load_optimal_moves()
