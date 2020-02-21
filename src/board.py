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

    def valid_move(self, position):
        return self.within_board(position) and not self.position_taken(position)

    def position_taken(self, position):
        return self.spaces[position] != None

    def within_board(self, position):
        result = position >= 0 and position <= Board.SIZE
        return result
