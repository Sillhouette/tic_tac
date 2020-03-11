import src.constants as constants
import math

class Minimax():
    def __init__(self, processor, maximizer_index):
        self.processor = processor 
        self.maximizer_index = maximizer_index

    def execute(self, depth, player_index, alpha=-math.inf, beta=math.inf):

        result = self.processor.move_result()
        if result != None:
            return self.score_move(result)

        if player_index == self.maximizer_index:
            best_score = -math.inf
            maximizer_token = self.processor.get_player_tokens()[self.maximizer_index]
            next_player_index = self.processor.next_player_index(player_index)
            for move in self.processor.get_valid_moves():
                self.processor.execute_move(move, maximizer_token)
                score = self.execute(depth + 1, next_player_index, alpha, beta)
                self.processor.execute_move(move, None)
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta >= alpha:
                    pass
            return best_score
        else:
            best_score = math.inf
            next_player_index = self.processor.next_player_index(player_index)
            minimizer_token = self.processor.get_player_tokens()[player_index]
            for move in self.processor.get_valid_moves():
                self.processor.execute_move(move, minimizer_token) 
                score = self.execute(depth + 1, next_player_index, alpha, beta)
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
        maximizer_token = self.processor.get_player_tokens()[self.maximizer_index]
        if result == maximizer_token:
            return 10
        elif result == constants.CATS:
            return 0
        else:
            return -10
