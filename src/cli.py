import src.constants as constants

class Cli():
    MESSAGES = {
        constants.WELCOME: "Hi! Welcome to Tic-Tac by Toenails Inc!",
        constants.EXIT: "Leaving so soon? Hope to see you back again shortly!",
        constants.FINISHED: "You played a great game! See you next time!",
        constants.ERROR: "\nI'm sorry, it seems you may have accidently made an invalid move, can you please try another position?",
        constants.WIN: (lambda token: f"{token} wins!"),
        constants.REQUEST_MOVE: (lambda token: f"It's {token}'s turn! Please select a square using 1-9:\n")
    }

    def __init__(self, writer=print, reader=input):
        self.writer = writer
        self.reader = reader

    def log(self, message):
        self.writer(message)

    def prompt_user(self, message=""):
        return self.reader(message).lower()

    def welcome(self):
        self.log(self.MESSAGES[constants.WELCOME])
        
    def handle_game_end(self):
        self.log(self.MESSAGES[constants.FINISHED])
        
    def handle_exit(self):
        self.log(self.MESSAGES[constants.EXIT])

    def get_player_tokens(self):
        return ["X", "O"]

    def get_board_type(self):
        return "3x3"
    
    def build_possible_results(self, players):
        results = { 
            constants.EXIT: self.MESSAGES[constants.EXIT],
            constants.FINISHED: self.MESSAGES[constants.FINISHED]
        }

        for player in players:
            results[player.token] = self.MESSAGES[constants.WIN](player.token) 

        return results
    
    def request_move(self, player):
         turn_prompt = self.MESSAGES[constants.REQUEST_MOVE](player.token) 
         return self.prompt_user(turn_prompt)

    def print_board(self, board):
        if board.type == "3x3":
            self.display_3x3_board(board)

    def display_3x3_board(self, board):
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

    def invalid_move(self):
        self.log(self.MESSAGES[constants.ERROR])

