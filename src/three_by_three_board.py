import src.constants as constants

class ThreeByThreeBoard():

    def __init__(self):
        self.type = constants.THREE_BY_THREE 
        self.size = 3 * 3
        self.spaces = [None] * self.size

    def turn_count(self):
        return self.size - self.spaces.count(None)

    def full(self):
        return not None in self.spaces

    def update(self, index, token):
        self.spaces[index] = token

    def token_at(self, position):
        return self.spaces[position]

    def position_taken(self, position):
        return self.spaces[position] != None

    def within_board(self, position):
        return position >= 0 and position <= self.size

