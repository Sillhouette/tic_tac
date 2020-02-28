import src.constants as constants

class Validator():

    def validate_move(self, move, board):
        if board.type == constants.THREE_BY_THREE:
            return self.validate_3x3(move, board)

    def validate_3x3(self, move, board):
        if move.lower() == constants.EXIT:
            return [constants.EXIT, None]
        elif self.validate_3x3_input(move, board) and self.validate_3x3_move(move, board):
             return [constants.MOVE, move] 
    
        return [constants.ERROR, move]

    def validate_3x3_input(self, move, board):
        valid_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        return move in valid_input  

    def validate_3x3_move(self, move, board):
        position = board.move_to_index(move)
        return self.within_board(position, board) and not self.position_taken(position, board)

    def position_taken(self, position, board):
        return board.spaces[position] != None

    def within_board(self, position, board):
        if board.type == constants.THREE_BY_THREE:
            return position >= 0 and position <= board.size
