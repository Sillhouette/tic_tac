from src.cli import Cli
from src.player import Player
from src.board_builder import BoardBuilder
from src.validator import Validator

class Game:
    def __init__(self, cli, players, board):
        self.cli = cli
        self.players = players
        self.board = board
        self.game_in_process = True
        self.possible_results = self.build_possible_results()
        self.actions = {
            Cli.MOVE: (lambda move, token: self.board.move_result(move, token)),
            Cli.EXIT: (lambda move, token: Cli.EXIT),
            Cli.ERROR: (lambda move, token: self.cli.log(Cli.MESSAGES[Cli.ERROR])) 
        } #contains lambdas

    def play(self):
        result = None
        validator = Validator()
        self.cli.print_board(self.board)
        while(self.game_in_process):
            current_player = self.current_player()
            selected_action, move = validator.validate_move(self.cli.request_move(current_player), self.board)
            result = self.actions[selected_action](move, current_player.token)
            if result != Cli.EXIT: self.cli.print_board(self.board)
            if result in self.possible_results or self.board.full(): self.game_in_process = False

        self.cli.log(self.possible_results[result])
   
    def current_player(self):
        num_players = len(self.players)
        turns_taken = self.board.turn_count()
        return self.players[turns_taken % num_players]

    def build_possible_results(self):
        results = { 
            Cli.EXIT: Cli.MESSAGES[Cli.EXIT],
            Cli.FINISHED: Cli.MESSAGES[Cli.FINISHED]
        }

        for player in self.players:
            results[player.token] = Cli.MESSAGES[Cli.WIN](player.token) 

        return results
