import src.constants as constants

class ThreeByThreeValidator():
    def __init__(self, processor):
        self.processor = processor

    def validate(self, move):
        move = move.lower()
        if self.validate_input(move):
            return self.processor.generate_move_action(move)

        return [constants.ERROR, move]

    def validate_input(self, move):
        valid_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "exit"]
        return move in valid_input  

