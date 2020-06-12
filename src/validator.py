import src.constants as constants

class Validator():
    def set_processor(self, processor):
        self.processor = processor

    def validate(self, move):
        move = move.lower()
        if self.validate_move(move):
            return self.processor.generate_move_action(move)

        return [constants.ERROR, move]

    def validate_move(self, move):
        valid_moves = self.generate_valid_options(self.processor.board.size)
        return move in valid_moves

    def generate_valid_options(self, num_options):
        size = range(1, num_options + 1)
        options = list(map(str, size))
        options.append(constants.EXIT)
        return options

