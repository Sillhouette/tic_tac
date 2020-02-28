from src.cli import Cli
from src.game import Game
from src.board_builder import BoardBuilder
from src.player_builder import PlayerBuilder

class App():
    def __init__(self, cli=Cli()):
        self.cli = cli

    def initialize(self):
        self.cli.welcome()
        players = self.setup_players()
        board = self.setup_board()
        game = Game(self.cli, players, board)
        game.play()
        #self.cli.handle_game_end()

    def setup_players(self):
        tokens = self.cli.get_player_tokens()
        builder = PlayerBuilder()
        players = builder.build_players(tokens)
        return players

    def setup_board(self):
        board_type = self.cli.get_board_type()
        builder = BoardBuilder()
        board = builder.build_board(board_type)
        return board