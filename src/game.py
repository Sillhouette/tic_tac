from src.cli import Cli
from src.board import Board
from src.player import Player

class Game():

    def __init__(self, cli=Cli(), board=Board(), players=[Player(token="X"),
                                                          Player(token="O")]):
        self.cli = cli
        self.board = board
        self.players = players
        self.exit = False
        self.safe_exit = False

    def start(self):
        self.cli.welcome()
        self.play()

    def play(self):
        self.cli.display_board(self.board)
        while not self.game_is_over():
            self.turn()
        self.handle_exit()

    def handle_exit(self):
        if self.exit:
            self.cli.handle_exit()
        elif self.safe_exit:
            self.cli.handle_safe_exit()
        else:
            self.cli.goodbye()
        
    def game_is_over(self):
        return self.exit or self.safe_exit or self.board.full()

    def turn(self, error=False, chances=1):
        if error: self.cli.invalid_move()
        
        if chances >= 5:
            self.safe_exit = True
            return
            
        player_choice = self.cli.prompt_player_turn(self.current_player())
        if player_choice == None:
            self.safe_exit = True
        elif player_choice.lower() == "exit":
            self.exit = True
        else:
            move = self.input_to_index(player_choice)
            if self.board.valid_move(move):
                self.board.update(move, self.current_player().token)
                self.cli.display_board(self.board)
            else:
                self.turn(True, chances + 1)
       
    def input_to_index(self, user_input):
        return int(user_input) - 1 

    def current_player(self):
        num_players = len(self.players)
        return self.players[self.board.turn_count() % num_players]

