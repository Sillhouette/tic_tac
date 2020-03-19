import sys
import src.constants as constants

from src.cli import Cli
from src.game import Game
from src.board import Board
from src.processor import Processor
from src.player_builder import PlayerBuilder

class App():
    def __init__(self, cli=Cli(), board=None, processor=None, players=[],
                 game=None):
        self.cli = cli
        self.board = board
        self.processor = processor
        self.players = players
        self.game = game

    def initialize(self):
        self.cli.welcome()
        self.setup_board()
        if not self.processor: self.processor = Processor(self.board)
        self.cli.set_dependencies(self.processor)
        self.setup_players()
        self.processor.set_players(self.players)
        self.game = Game(self.cli, self.players, self.board, self.processor)
        self.game.play()
        self.cli.handle_replay()

    def setup_players(self):
        tokens = self.cli.get_player_tokens()
        choice = self.cli.get_opponent_choice()
        self.check_choice_for_exit(choice)
        builder = PlayerBuilder(self.processor, self.cli)
        players = builder.build_players(tokens, choice)
        self.players = players

    def setup_board(self):
        board_choice = self.cli.get_board_type()
        self.check_choice_for_exit(board_choice)
        chosen_board = int(board_choice) - 1
        board_type = constants.BOARD_CHOICES[chosen_board]
        self.board = Board(board_type)

    def check_choice_for_exit(self, choice):
        if choice == constants.EXIT:
            self.exit_app()

    def exit_app(self):
        self.cli.handle_exit()
        sys.exit()
