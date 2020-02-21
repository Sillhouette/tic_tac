from src.cli import Cli
from src.board import Board
from src.player import Player

class Game():

    def __init__(self, cli=Cli(), board=Board(), players=[Player(token="X"),
                                                          Player(token="O")]):
        self.cli = cli
        self.board = board
        self.players = players

    def start(self):
        self.cli.welcome()
        self.play()

    def play(self):
        self.cli.display_board(self.board)
        while not self.board.full():
            self.turn()

        self.cli.goodbye()
    
    def turn(self, error=False):
        if error: self.cli.invalid_move()

        player_choice = self.cli.prompt_player_turn(self.current_player())
        move = self.input_to_index(player_choice)
        if self.board.valid_move(move):
            self.board.update(move, self.current_player().token)
            self.cli.display_board(self.board)
        else:
            self.turn(True)
       
    def input_to_index(self, user_input):
        return int(user_input) - 1 

    def current_player(self):
        num_players = len(self.players)
        return self.players[self.board.turn_count() % num_players]

