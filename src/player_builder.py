from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer

class PlayerBuilder():
    def __init__(self, validator, processor, cli):
        self.processor = processor
        self.validator = validator
        self.cli = cli

    def build_players(self, player_tokens):
        players = []
        players.append(HumanPlayer(self.cli, self.validator, player_tokens[0]))
        players.append(ComputerPlayer(self.processor, self.cli, player_tokens[1]))

        return players

