import random
import src.constants as constants

class ComputerPlayer():
    def __init__(self, board, token="O"):
        self.token = token
        self.board = board
        
    def set_token(self, token):
        self.token = token

    def get_move(self):
        valid_space = False
        
        while valid_space == False:
            choice = random.randint(1, 9)
            index = self.board.move_to_index(choice)
            if not self.board.position_taken(index):
                valid_space = str(choice)
                
        return [constants.MOVE, choice]

