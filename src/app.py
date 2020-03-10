from src.cli import Cli
from src.game import Game
from src.board_builder import BoardBuilder
from src.player_builder import PlayerBuilder
from src.validator_builder import ValidatorBuilder
from src.processor_builder import ProcessorBuilder

class App():
    def __init__(self, cli=Cli(), board=None, processor=None, validator=None, players=[],
                 game=None):
        self.cli = cli
        self.board = board
        self.processor = processor
        self.validator = validator
        self.players = players
        self.game = game

    def initialize(self):
        self.cli.welcome()
        self.setup_board()
        self.cli.set_presenter_type(self.board.type)
        self.setup_processor()
        self.setup_validator()
        self.setup_players()
        self.processor.set_players(self.players)
        self.game = Game(self.cli, self.players, self.board, self.validator, self.processor)
        self.game.play()
        self.cli.handle_replay()

    def setup_players(self):
        tokens = self.cli.get_player_tokens()
        builder = PlayerBuilder(self.validator, self.processor, self.cli)
        players = builder.build_players(tokens)

        self.players = players

    def setup_board(self):
        board_type = self.cli.get_board_type()
        builder = BoardBuilder()
        board = builder.build_board(board_type)
        self.board = board

    def setup_validator(self):
        builder = ValidatorBuilder()
        self.validator = builder.build_validator(self.processor)

    def setup_processor(self):
        builder = ProcessorBuilder()
        self.processor = builder.build_processor(self.board)
