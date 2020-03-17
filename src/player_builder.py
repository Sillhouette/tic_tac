import src.constants as constants

from src.human_player import HumanPlayer
from src.computer_player import ComputerPlayer

class PlayerBuilder():
    def __init__(self, validator, processor, cli):
        self.processor = processor
        self.validator = validator
        self.cli = cli

    def build_players(self, player_tokens):
        choice = self.get_valid_choice()

        player_1 = self.build_human_player(player_tokens[0])
        if choice == "1":
            player_2 = self.build_human_player(player_tokens[1])
        elif choice == "2":
            player_2 = self.build_easy_computer()
        elif choice == "3":
            player_2 = self.build_hard_computer()
        else:
            return constants.EXIT
        return [player_1, player_2]

    def get_valid_choice(self):
        valid_choices = ["1", "2", "3", "exit"]
        choice = None
        while not choice in valid_choices:
            choice = self.cli.get_opponent()
        return choice

    def build_easy_computer(self):
        return ComputerPlayer(self.processor, self.cli,
                              difficulty=constants.EASY)

    def build_hard_computer(self):
        return ComputerPlayer(self.processor, self.cli)

    def build_human_player(self, token):
        return HumanPlayer(self.cli, self.validator, token=token)
