from src.cli import Cli

class HumanPlayer():
    def __init__(self, cli, validator, name="player", token="X"):
        self.token = token
        self.name = name
        self.cli = cli
        self.validator = validator
    
    def set_token(self, token):
       self.token = token

    def get_move(self):
        move = self.cli.request_move(self)
        return self.validate_move(move)

    def validate_move(self, move):
        return self.validator.validate(move)
