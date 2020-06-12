import json
import src.constants as constants

from src.board import Board
from src.processor import Processor
from src.human_player import HumanPlayer
from src.minimax import Minimax
from src.cli import Cli
from src.game import Game

class DataGatherer():
    def __init__(self):
        self.data = {}

    def gather_3x3_info(self):
        cli = Cli()
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        player_1 = HumanPlayer(cli)
        player_2 = HumanPlayer(cli, token="O")
        processor.set_players([player_1, player_2])
        self.minimax = Minimax(processor, 0, self)

    def initialize(self):
        self.setup()
        self.minimax.get_best_move(0, 0)
        self.write_3x3_data_to_file()

    def store_result(self, board_state, move, writing=False):
        board_state_string = self.stringify_state(board_state) 
        self.data[board_state_string] = move
        if writing:
            self.write_3d_data_to_file()

    def stringify_state(self, board_state):
        scrubbed_state = ["_" if token is None else token for token in board_state]
        return "".join(scrubbed_state)

    def write_3d_data_to_file(self):
        json_object = json.dumps(self.data, indent=4)

        with open(f"{constants.THREE_DIMENSIONAL}_optimal_moves.json", "w") as outfile:
            outfile.write(json_object)

    def write_3x3_data_to_file(self):
        json_object = json.dumps(self.data, indent=4)

        with open(f"{constants.THREE_BY_THREE}_optimal_moves.json", "w") as outfile:
            outfile.write(json_object)
