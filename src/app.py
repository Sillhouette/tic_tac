from src.cli import Cli
from src.game import Game
from src.board_builder import BoardBuilder
from src.player_builder import PlayerBuilder
from src.validator_builder import ValidatorBuilder

class App():
    def __init__(self, cli=Cli(), board=None, validator=None, players=[],
                 game=None):
        self.cli = cli
        self.board = board
        self.validator = validator
        self.players = players
        self.game = game

    def initialize(self):
        self.cli.welcome()
        self.setup_board()
        self.cli.set_presenter_type(self.board.type)
        self.setup_validator()
        self.setup_players()
        self.game = Game(self.cli, self.players, self.board, self.validator)
        self.game.play()
        self.cli.handle_replay()

    def setup_players(self):
        tokens = self.cli.get_player_tokens()
        builder = PlayerBuilder(self.validator, self.board, self.cli)
        players = builder.build_players(tokens)

        self.players = players

    def setup_board(self):
        board_type = self.cli.get_board_type()
        builder = BoardBuilder()
        board = builder.build_board(board_type)
        self.board = board

    def setup_validator(self):
        builder = ValidatorBuilder()

        self.validator = builder.build_validator(self.board)

