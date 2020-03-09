import src.constants as constants

class ThreeByThreePresenter():

    def __init__(self):
        self.border = "⊱ –––––– {⋆⌘⋆} –––––– ⊰"
        self.divider = "      ---+---+---"

    def colorize_empty_space_index(self, index):
        return f"{constants.EMPTY_INDEX_COLOR_START}{index}{constants.EMPTY_INDEX_COLOR_END}"
    
    def scrub_board(self, board):
        scrubbed_board = []
        for i, token in enumerate(board.spaces, start=1):
            if token == None:
                scrubbed_board.append(self.colorize_empty_space_index(i))
            else:
                scrubbed_board.append(token)
        return scrubbed_board

    def present_board(self, board):
        scrubbed_board = self.scrub_board(board)
        return f"""
{self.border}

       {scrubbed_board[0]} | {scrubbed_board[1]} | {scrubbed_board[2]} 
{self.divider}
       {scrubbed_board[3]} | {scrubbed_board[4]} | {scrubbed_board[5]} 
{self.divider}
       {scrubbed_board[6]} | {scrubbed_board[7]} | {scrubbed_board[8]} 

{self.border}
"""

