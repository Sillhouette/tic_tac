import src.constants as constants

from src.three_by_three_presenter import ThreeByThreePresenter

class Cli():
    MESSAGES = {
        constants.WELCOME: "Hi! Welcome to Tic-Tac by Toenails Inc!",
        constants.EXIT: "Leaving so soon? Hope to see you back again shortly!",
        constants.FINISHED: "You played a great game! See you next time!",
        constants.ERROR: "\nI'm sorry, it seems you may have accidently made an invalid move, can you please try another position?",
        constants.WIN: (lambda token: f"{token} wins!"),
        constants.REQUEST_MOVE: (lambda token: f"It's {token}'s turn! Please select a square using 1-9:\n")
    }

    def __init__(self, writer=print, reader=input):
        self.writer = writer
        self.reader = reader

    def set_presenter_type(self, board_type):
        if board_type == constants.THREE_BY_THREE:
            self.presenter = ThreeByThreePresenter()

    def log(self, message):
        self.writer(message)

    def prompt_user(self, message=""):
        return self.reader(message).lower()

    def welcome(self):
        self.log(self.MESSAGES[constants.WELCOME])
        
    def handle_game_end(self):
        self.log(self.MESSAGES[constants.FINISHED])
        
    def handle_exit(self):
        self.log(self.MESSAGES[constants.EXIT])

    def print_board(self, board):
        self.log(self.presenter.present_board(board))

    def invalid_move(self):
        self.log(self.MESSAGES[constants.ERROR])

    def request_move(self, player):
         turn_prompt = self.MESSAGES[constants.REQUEST_MOVE](player.token)
         return self.prompt_user(turn_prompt)

    def get_player_tokens(self):
        return ["X", "O"]

    def get_board_type(self):
        return constants.THREE_BY_THREE
    
    def build_possible_results(self, players):
        results = { 
            constants.EXIT: self.MESSAGES[constants.EXIT],
            constants.FINISHED: self.MESSAGES[constants.FINISHED]
        }

        for player in players:
            results[player.token] = self.MESSAGES[constants.WIN](player.token) 

        return results

