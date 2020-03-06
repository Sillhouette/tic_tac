from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer

class PlayerBuilder():
    def __init__(self, validator, board, cli):
        self.board = board
        self.validator = validator
        self.cli = cli

    def build_players(self, player_tokens):
        players = []
        players.append(HumanPlayer(self.cli, self.validator, player_tokens[0]))
        players.append(ComputerPlayer(self.board, self.cli, player_tokens[1]))
        #for token in player_tokens:
        #    players.append(Player(cli, token))

        return players


