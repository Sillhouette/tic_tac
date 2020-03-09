import src.constants as constants

class ThreeByThreeProcessor():
    # => All of the possible winning combinations
    WIN_COMBINATIONS = {
        "Top Row": [0, 1, 2],
        "Middle Row": [3, 4, 5],
        "Bottom Row": [6, 7, 8],
        "First Column": [0, 3, 6],
        "Second Column": [1, 4, 7],
        "Third Column": [2, 5, 8],
        "Left to Right Diagonal": [0, 4, 8],
        "Right to Left Diagonal": [2, 4, 6]
    }

    def __init__(self, board):
        self.board = board

    def move_to_index(self, move):
        return int(move) - 1

    def get_valid_moves(self):
        return [index + 1 for index, space in enumerate(self.board.spaces) if space == None]

    def valid_move(self, move):
        position = self.move_to_index(move)
        return self.board.within_board(position) and not self.board.position_taken(position)

    def execute_move(self, move, token):
        index = self.move_to_index(move)
        self.board.update(index, token)
        return self.move_result()

    def move_result(self):
        winner = self.winner()
        if winner: return winner
        elif self.cats_game(): return constants.CATS 

    def cats_game(self):
        return self.board.full() and not self.winner()

    def generate_move_action(self, move):
        if move == constants.EXIT:
            return [constants.EXIT, None]
        elif self.valid_move(move):
            return [constants.MOVE, move]
        
        return [constants.ERROR, move]

    def compare_board_indicies(self, index_1, index_2):
        return self.board.token_at(index_1) == self.board.token_at(index_2)

    def winner(self):
        winner = None
        for combo in self.WIN_COMBINATIONS.values():
            win_index_1, win_index_2, win_index_3 = combo
            if self.compare_board_indicies(win_index_1, win_index_2) and\
                self.compare_board_indicies(win_index_2, win_index_3) and\
                self.board.position_taken(win_index_1):
                winner = self.board.token_at(win_index_1)

        return winner

