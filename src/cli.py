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
    
    def prompt_user(self, message="", chances=1):
        user_input = self.reader(message)
        error_message = "It seems you may have entered some invalid input. Please try again:\n"
        
        if chances >= 5:
            return
        
        if self.validate_input(user_input):
            return user_input
        else:
            return self.prompt_user(error_message, chances + 1)

    def validate_input(self, user_input):
        valid_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "exit"]
        return user_input in valid_input 

    def welcome(self):
        self.log("Hi! Welcome to Tic-Tac by Toenails Inc!")
        
    def goodbye(self):
        self.log("You played a great game! See you next time!")
        
    def handle_exit(self):
        self.log("Leaving so soon? Hope to see you back again shortly!")

    def handle_safe_exit(self):
        self.log("I'm sorry, there has been too many invalid inputs in a row, please start a new game :)")

    def prompt_player_turn(self, player):
         turn_prompt = f"It's {player.token}'s turn! Please select a square using 1-9:\n"
         player_input = self.prompt_user(turn_prompt)
         return player_input

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

    def invalid_move(self):
        error = "\nI'm sorry, it seems you may have accidently made an invalid move, can you please try another position?\n"
        self.log(error)

