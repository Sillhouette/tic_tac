from src.cli import Cli

class HumanPlayer():
    def __init__(self, cli, name="player", token="X"):
        self.token = token
        self.name = name
        self.cli = cli
    
    def set_token(self, token):
       self.token = token

    def get_move(self):
        return self.cli.request_move(self)

