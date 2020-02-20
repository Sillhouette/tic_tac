class Cli():
    
    def __init__(self, writer=print, reader=input):
        self.writer = writer
        self.reader = reader

    def log(self, message):
        if isinstance(message, list):
            self.log_messages(message)
        else:
            self.log_message(message)

    def log_message(self, message):
        self.writer(message)

    def log_messages(self, messages):
        for message in range(len(messages)):
            self.writer(messages[message])
    
    def prompt_user(self, message=""):
        return self.reader(message)

    def welcome(self):
        self.log("Hi! Welcome to Tic-Tac-Toe by Toenails Inc!")
        
    def goodbye(self):
        self.log("You played a great game! See you next time!")
