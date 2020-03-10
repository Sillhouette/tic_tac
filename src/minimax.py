import src.constants as constants
import math

class Minimax():
    def __init__(self, processor, maximizer_token):
        self.maximizer_token = maximizer_token
        self.processor = processor 

    def execute(self, depth, isMaximizing, alpha=-math.inf, beta=math.inf):

        result = self.processor.move_result()
        if result != None:
            return self.score_move(result)

        if isMaximizing:
            best_score = -math.inf
            for move in self.processor.get_valid_moves():
                self.processor.execute_move(move, self.maximizer_token)
                score = self.execute(depth + 1, False, alpha, beta)
                self.processor.execute_move(move, None)
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta >= alpha:
                    pass
            return best_score
        else:
            best_score = math.inf
            for move in self.processor.get_valid_moves():
                self.processor.execute_move(move, self.get_minimizer_token()) 
                score = self.execute(depth + 1, True, alpha, beta)
                self.processor.execute_move(move, None)
                best_score = min(score, best_score)
                beta = min(beta, score)
                if alpha >= beta:
                    pass

            return best_score

    def get_minimizer_token(self):
        return [player.token for player in self.processor.players if
                player.token != self.maximizer_token][0]

    def score_move(self, result):
        if result == self.maximizer_token:
            return 10
        elif result == constants.CATS:
            return 0
        else:
            return -10
