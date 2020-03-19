import src.constants as constants

from src.three_by_three_presenter import ThreeByThreePresenter
from src.three_dimensional_presenter import ThreeDimensionalPresenter
from src.validator import Validator

class Cli():
    MESSAGES = {
        constants.WELCOME: "Hi! Welcome to Tic-Tac by Toenails Inc!",
        constants.COMPUTER_TURN: "It's the computer player's turn now! His move is:",
        constants.EXIT: "Leaving so soon? Hope to see you back again shortly!",
        constants.CATS: "Cats game! You all played phenomenally!",
        constants.ERROR: "\nI'm sorry, it seems you may have accidently made an invalid move, can you please try another position?",
        constants.OPTION_ERROR: "\nI'm sorry, it seems you may have accidently chosen an invalid option, can you please try another one?\n",
        constants.WIN: (lambda token: f"Congratulations {token}! you win!"),
        constants.REQUEST_MOVE: (lambda token: f"It's {token}'s turn! Please select a square using 1-9:\n"),
        constants.REPLAY: "\nTo play a new game please restart the app with the command 'python3 run_game.py'"
    }

    def __init__(self, writer=print, reader=input, validator=Validator()):
        self.writer = writer
        self.reader = reader
        self.validator = validator

    def set_dependencies(self, processor):
        if processor.board.type == constants.THREE_BY_THREE:
            self.presenter = ThreeByThreePresenter()
        elif processor.board.type == constants.THREE_DIMENSIONAL:
            self.presenter = ThreeDimensionalPresenter()
        self.validator.set_processor(processor)

    def log(self, message):
        self.writer(message)

    def prompt_user(self, message=""):
        return self.reader(message).lower()

    def welcome(self):
        self.log(self.MESSAGES[constants.WELCOME])

    def notify_for_computer_turn(self):
        self.log(self.MESSAGES[constants.COMPUTER_TURN])
        
    def handle_cats_game(self):
        self.log(self.MESSAGES[constants.CATS])

    def handle_replay(self):
        self.log(self.MESSAGES[constants.REPLAY])
        
    def handle_exit(self):
        self.log(self.MESSAGES[constants.EXIT])

    def print_board(self, board):
        self.log(self.presenter.present_board(board))

    def invalid_move(self):
        self.log(self.MESSAGES[constants.ERROR])

    def invalid_option(self):
        self.log(self.MESSAGES[constants.OPTION_ERROR])

    def request_move(self, player):
         turn_prompt = self.MESSAGES[constants.REQUEST_MOVE](player.token)
         move = self.prompt_user(turn_prompt)
         return self.validator.validate(move) 

    def get_opponent_choice(self):
        num_options = len(constants.OPPONENTS)
        valid_choices = self.validator.generate_valid_options(num_options)
        choice = None
        while not choice in valid_choices:
            if choice != None: self.invalid_option()
            choice = self.get_opponent()
        return choice

    def get_opponent(self):
        return self.prompt_user(self.generate_opponent_menu())

    def generate_opponent_menu(self):
        opponents = list(constants.OPPONENTS.values())
        menu = "Choose your opponent:\n"
        for index, opponent in enumerate(opponents):
            menu += f"  {index + 1}. {opponent}\n"
        return menu

    def get_player_tokens(self):
        return ["X", "O"]

    def get_board_type(self):
        num_options = len(constants.BOARD_CHOICES)
        valid_choices = self.validator.generate_valid_options(num_options)
        choice = None
        while not choice in valid_choices:
            if choice != None: self.invalid_option()
            choice = self.prompt_user(self.generate_board_menu())
        return choice

    def generate_board_menu(self):
        prompt = "Choose your board:\n"
        choices = constants.BOARD_CHOICES
        for index, choice in enumerate(choices):
            prompt += f" {index + 1}. {choice} board\n"
        return prompt

    def build_possible_results(self, players):
        results = { 
            constants.EXIT: self.MESSAGES[constants.EXIT],
            constants.CATS: self.MESSAGES[constants.CATS]
        }

        for player in players:
            results[player.token] = self.MESSAGES[constants.WIN](player.token) 

        return results

