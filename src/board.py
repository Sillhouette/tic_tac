class Board:
    SIZE = 9

    def __init__(self):
        self.spaces = [None] * Board.SIZE 

    def full(self):
        return not None in self.spaces

    def update(self, index, token):
        self.spaces[index] = token

    def turn_count(self):
        return Board.SIZE - self.spaces.count(None)
