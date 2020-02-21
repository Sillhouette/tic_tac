class Cli():
    board_border = "⊱ –––––– {⋆⌘⋆} –––––– ⊰",
    board_divider = "      ---+---+---"

    def __init__(self, writer=print, reader=input):
        self.writer = writer
        self.reader = reader

    def log(self, message):
        if isinstance(message, list):
            self.log_messages(message)
        else:
            self.log_message(message)

    def log_message(self, message):
        self.writer(message)

    def log_messages(self, messages):
        for message in range(len(messages)):
            self.writer(messages[message])
    
    def prompt_user(self, message=""):
        return self.reader(message)

    def welcome(self):
        self.log("Hi! Welcome to Tic-Tac-Toe by Toenails Inc!")
        
    def goodbye(self):
        self.log("You played a great game! See you next time!")

    def display_board(self, board):
        board = f"""\

       {board.spaces[0]} | {board.spaces[1]} | {board.spaces[2]} 
{Cli.board_divider}
       {board.spaces[3]} | {board.spaces[4]} | {board.spaces[5]} 
{Cli.board_divider}
       {board.spaces[6]} | {board.spaces[7]} | {board.spaces[8]} 
\
"""
        self.log(board)
        return board

