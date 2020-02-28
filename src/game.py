import src.constants as constants

from src.cli import Cli
from src.player import Player
from src.validator import Validator

class Game:
    def __init__(self, cli, players, board):
        self.cli = cli
        self.players = players
        self.board = board
        self.game_in_process = True
        self.possible_results = self.cli.build_possible_results(self.players)
        self.actions = {
            constants.MOVE: (lambda move, token: self.board.move_result(move, token)),
            constants.EXIT: (lambda move, token: constants.EXIT),
            constants.ERROR: (lambda move, token: self.cli.invalid_move()) 
        } #contains lambdas

    def play(self):
        result = None
        validator = Validator()
        self.cli.print_board(self.board)
        while(self.game_in_process):
            current_player = self.current_player()
            player_choice = self.cli.request_move(current_player)
            selected_action, move = validator.validate_move(player_choice, self.board)
            result = self.actions[selected_action](move, current_player.token)
            if result != constants.EXIT: self.cli.print_board(self.board)
            if result in self.possible_results: self.game_in_process = False

        self.cli.log(self.possible_results[result])
   
    def current_player(self):
        num_players = len(self.players)
        turns_taken = self.board.turn_count()
        return self.players[turns_taken % num_players]

