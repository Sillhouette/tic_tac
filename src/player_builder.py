from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer

class PlayerBuilder():
    def __init__(self, validator, processor, cli):
        self.processor = processor
        self.validator = validator
        self.cli = cli

    def build_players(self, player_tokens):
        human_player_first = HumanPlayer(self.cli, self.validator, token=player_tokens[0])
        human_player_second = HumanPlayer(self.cli, self.validator, token=player_tokens[1])
        computer_first_player = ComputerPlayer(self.processor, self.cli, player_tokens[0])
        computer_second_player = ComputerPlayer(self.processor, self.cli, player_tokens[1])
        #return [human_player_first, human_player_second]
        #return [computer_first_player, computer_second_player]
        return [human_player_first, computer_second_player] 
        #return [computer_first_player, human_player_second]

