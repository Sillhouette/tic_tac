import src.constants as constants

class ThreeDimensionalPresenter():

    def __init__(self):
        self.border = "⊱ –––––––––––––––––––––––––– {⋆⌘⋆} –––––––––––––––––––––––––– {⋆⌘⋆} –––––––––––––––––––––––––– ⊰"
        self.divider = "------+------+------"
        self.spaces = "     "

    def colorize_empty_space_index(self, index):
        if index < 10:
            index = f"0{index}"
        return f"{constants.EMPTY_INDEX_COLOR_START}{index}{constants.EMPTY_INDEX_COLOR_END}"
    
    def scrub_board(self, board):
        scrubbed_board = []
        for i, token in enumerate(board.spaces, start=1):
            if token == None:
                scrubbed_board.append(self.colorize_empty_space_index(i))
            else:
                scrubbed_board.append(" " + token)
        return scrubbed_board

    def present_board(self, board):
        scrubbed_board = self.scrub_board(board)
        return f"""
{self.border}

{self.spaces}  {scrubbed_board[0]}  |  {scrubbed_board[1]}  |  {scrubbed_board[2]}  {self.spaces}   {self.spaces}  {scrubbed_board[9]}  |  {scrubbed_board[10]}  |  {scrubbed_board[11]}  {self.spaces}   {self.spaces}  {scrubbed_board[18]}  |  {scrubbed_board[19]}  |  {scrubbed_board[20]}
{self.spaces}{self.divider}{self.spaces}   {self.spaces}{self.divider}{self.spaces}   {self.spaces}{self.divider}
{self.spaces}  {scrubbed_board[3]}  |  {scrubbed_board[4]}  |  {scrubbed_board[5]}  {self.spaces}   {self.spaces}  {scrubbed_board[12]}  |  {scrubbed_board[13]}  |  {scrubbed_board[14]}  {self.spaces}   {self.spaces}  {scrubbed_board[21]}  |  {scrubbed_board[22]}  |  {scrubbed_board[23]}
{self.spaces}{self.divider}{self.spaces}   {self.spaces}{self.divider}{self.spaces}   {self.spaces}{self.divider}
{self.spaces}  {scrubbed_board[6]}  |  {scrubbed_board[7]}  |  {scrubbed_board[8]}  {self.spaces}   {self.spaces}  {scrubbed_board[15]}  |  {scrubbed_board[16]}  |  {scrubbed_board[17]}  {self.spaces}   {self.spaces}  {scrubbed_board[24]}  |  {scrubbed_board[25]}  |  {scrubbed_board[26]} 

{self.border}
"""

