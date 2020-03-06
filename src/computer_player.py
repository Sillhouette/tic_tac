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

        valid_space = False
        
        while valid_space == False:
            choice = random.randint(1, 9)
            index = self.board.move_to_index(choice)
            if not self.board.position_taken(index):
                valid_space = str(choice)
                
        return [constants.MOVE, choice]

