from src.cli import Cli
from src.board import Board
from src.player import Player

class Game():

    def __init__(self, cli=Cli(), board=Board(), players=[Player(), Player()]):
        self.cli = cli
        self.board = board
        self.players = players

    def start(self):
        self.cli.welcome()
        self.play()

    def play(self):
        self.cli.log(self.board.stringify_spaces())
        while not self.board.full():
            self.turn()

        self.cli.goodbye()
    
    def turn(self):
        player_choice = self.cli.prompt_user()
        move = self.input_to_index(player_choice)

        self.board.update(move, self.current_player().token)
        self.cli.log(self.board.stringify_spaces())
       
    def input_to_index(self, user_input):
        return int(user_input) - 1 

    def current_player(self):
        num_players = len(self.players)
        return self.players[self.board.turn_count() % num_players]

