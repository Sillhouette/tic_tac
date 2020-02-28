class Player():
    def __init__(self, name="player", token="X"):
        self.name = name
        self.token = token
    
    def set_token(self, token):
       self.token = token
