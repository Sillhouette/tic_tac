class ThreeByThreeBoard():

    def __init__(self):
        self.type = "3x3"
        self.size = 9
        self.spaces = [None] * self.size

    def turn_count(self):
        return self.size - self.spaces.count(None)
    
    def move_result(self, move, token):
        self.update(move, token)
        if self.full(): return "finished"

    def full(self):
        return not None in self.spaces

    def update(self, move, token):
        index = self.move_to_index(move)
        self.spaces[index] = token

    def move_to_index(self, move):
        return int(move) - 1
