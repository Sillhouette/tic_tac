class Cli():
  
    def log(self, message, writer=print):
        if isinstance(message, list):
            self.log_messages(message, writer)
        else:
            self.log_message(message, writer)

    def log_message(self, message, writer=print):
        writer(message)

    def log_messages(self, messages, writer=print):
        for message in range(len(messages)):
            writer(messages[message])
    
    def welcome(self):
        log("Hi! Welcome to Tic-Tac-Toe by Toenails Inc!")
        
    def goodbye(self):
        log("You played a great game! See you next time!")
