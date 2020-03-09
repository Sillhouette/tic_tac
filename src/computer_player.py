import random
import src.constants as constants

class ComputerPlayer():
    def __init__(self, board, cli, token="O"):
        self.token = token
        self.board = board
        self.cli = cli
        
    def set_token(self, token):
        self.token = token

    def get_move(self):
        self.cli.notify_for_computer_turn()

        choice = random.choice(self.board.get_valid_moves())

        return [constants.MOVE, str(choice)]

