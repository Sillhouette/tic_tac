class Board:
    SIZE = 9
    border = "⊱ –––––– {⋆⌘⋆} –––––– ⊰",
    space = " "

    def __init__(self):
        self.spaces = [Board.space] * 9

    def full(self):
        return not Board.space in self.spaces

    def update(self, index, token):
        self.spaces[index] = token

    def turn_count(self):
        return Board.SIZE - self.spaces.count(Board.space)
