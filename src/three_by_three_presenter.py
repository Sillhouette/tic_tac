class ThreeByThreePresenter():

    def __init__(self):
        self.border = "⊱ –––––– {⋆⌘⋆} –––––– ⊰"
        self.divider = "      ---+---+---"
    
    def present_board(self, board):
        scrubbed_board = [token if token != None else " " for token in
                          board.spaces]

        return f"""
{self.border}

       {scrubbed_board[0]} | {scrubbed_board[1]} | {scrubbed_board[2]} 
{self.divider}
       {scrubbed_board[3]} | {scrubbed_board[4]} | {scrubbed_board[5]} 
{self.divider}
       {scrubbed_board[6]} | {scrubbed_board[7]} | {scrubbed_board[8]} 

{self.border}
"""

