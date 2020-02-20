<<<<<<< Updated upstream
class Game():
    pass
=======
from src.cli import Cli
from src.board import Board
from src.player import Player

class Game():

    def __init__(self, cli=Cli(), board=Board(), player_1=Player(),
                 player_2=Player()):
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
    
    def turn(self):
        move = self.cli.prompt_move()
        self.board.update(current_player.token())
        self.cli.log(self.board.stringify_spaces())
        
>>>>>>> Stashed changes
