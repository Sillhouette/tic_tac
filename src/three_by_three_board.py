import src.constants as constants

class ThreeByThreeBoard():
    # => All of the possible winning combinations
    WIN_COMBINATIONS = [
        [0, 1, 2], # Top row
        [3, 4, 5], # Middle row
        [6, 7, 8], # Bottom row
        [0, 3, 6], # First column
        [1, 4, 7], # Second column
        [2, 5, 8], # Third Column
        [0, 4, 8], # Left to Right diagonal
        [2, 4, 6]  # Right to Left diagonal
    ]

    def __init__(self):
        self.type = constants.THREE_BY_THREE 
        self.size = 9
        self.spaces = [None] * self.size

    def turn_count(self):
        return self.size - self.spaces.count(None)
    
    def move_result(self, move, token):
        self.update(move, token)
        winner = self.winner()
        if winner: return winner
        elif self.full(): return constants.CATS 

    def full(self):
        return not None in self.spaces

    def update(self, move, token):
        index = self.move_to_index(move)
        self.spaces[index] = token

    def move_to_index(self, move):
        return int(move) - 1

    def valid_move(self, move):
        position = self.move_to_index(move)
        return self.within_board(position) and not self.position_taken(position)

    def position_taken(self, position):
        return self.spaces[position] != None

    def within_board(self, position):
        return position >= 0 and position <= self.size

    def winner(self):
        winner = None
        for combo in self.WIN_COMBINATIONS:
            win_index_1, win_index_2, win_index_3 = combo
            if self.spaces[win_index_1] == self.spaces[win_index_2] and\
                self.spaces[win_index_2] == self.spaces[win_index_3] and\
                self.position_taken(win_index_1):
                winner = self.spaces[win_index_1]

        return winner
