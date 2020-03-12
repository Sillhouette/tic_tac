import src.constants as constants

from src.cli import Cli

class Game:
    def __init__(self, cli, players, board, processor):
        self.cli = cli
        self.players = players
        self.board = board
        self.processor = processor
        self.game_in_process = True
        self.possible_results = self.cli.build_possible_results(self.players)
        self.actions = {
            constants.MOVE: (lambda move, token: self.processor.execute_move(move, token)),
            constants.EXIT: (lambda move, token: constants.EXIT),
            constants.ERROR: (lambda move, token: self.cli.invalid_move()) 
        } #contains lambdas

    def play(self):
        result = None
        self.cli.print_board(self.board)
        while(self.game_in_process):
            current_player = self.processor.current_player()
            selected_action, move = current_player.get_move()
            result = self.actions[selected_action](move, current_player.token)
            if not self.player_chose_exit(result): self.cli.print_board(self.board)
            if self.game_over(result): self.game_in_process = False

        self.cli.log(self.possible_results[result])
    
    def player_chose_exit(self, result):
        return result == constants.EXIT

    def game_over(self, result):
        return result in self.possible_results

