class Cli():

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
        border = "⊱ –––––– {⋆⌘⋆} –––––– ⊰"
        divider = "      ---+---+---"
        scrubbed_board = [token if token != None else " " for token in
                          board.spaces]

        board_string = f"""
{border}

       {scrubbed_board[0]} | {scrubbed_board[1]} | {scrubbed_board[2]} 
{divider}
       {scrubbed_board[3]} | {scrubbed_board[4]} | {scrubbed_board[5]} 
{divider}
       {scrubbed_board[6]} | {scrubbed_board[7]} | {scrubbed_board[8]} 

{border}
"""
        self.log(board_string)
        return board_string

