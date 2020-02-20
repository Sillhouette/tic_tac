class Board:
    border = "⊱ –––––– {⋆⌘⋆} –––––– ⊰",
    divider = "      ---+---+---"
    space = " "
    
    def __init__(self):
        self.spaces = [Board.space] * 9

    def stringify_spaces(self):
        return [
            #Board.border,
            "",
            f"       {self.spaces[0]} | {self.spaces[1]} | {self.spaces[2]} ",
            Board.divider,
            f"       {self.spaces[3]} | {self.spaces[4]} | {self.spaces[5]} ", 
            Board.divider,
            f"       {self.spaces[6]} | {self.spaces[7]} | {self.spaces[8]} ",
            "",
            #Board.border 
        ]
    
    def full(self):
        return not Board.space in self.spaces
