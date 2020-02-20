from src.cli import Cli
from src.board import Board
from src.player import Player

class Game():

    def __init__(self, cli=Cli(), board=Board(), player_1=Player(token="X"),
                 player_2=Player(token="O")):
        self.cli = cli
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2

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
        move = self.input_to_index(int(player_choice))

        self.board.update(move, self.current_player().token)
        self.cli.log(self.board.stringify_spaces())
       
    def input_to_index(self, user_input):
        return user_input - 1 

    def current_player(self):
        if self.board.turn_count() % 2 == 0:
            return self.player_1
        else:
            return self.player_2

