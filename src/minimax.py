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
            return self.calculate_best_score(depth, player_index, alpha, beta, best_score,
                                 self.prune_alpha, max)
        else:
            best_score = math.inf
            return self.calculate_best_score(depth, player_index, alpha, beta, best_score,
                                 self.prune_beta, min)

    def calculate_best_score(self, depth, player_index, alpha,
                             beta, default_score, prune, compare):
        best_score = default_score
        token = self.processor.get_player_tokens()[player_index]
        next_player_index = self.processor.next_player_index(player_index)
        for move in self.processor.get_valid_moves():
            self.processor.execute_move(move, token)
            score = self.execute(depth + 1, next_player_index, alpha, beta)
            self.processor.execute_move(move, None)
            best_score = compare(score, best_score)
            if prune(best_score, alpha, beta):
                pass
        return best_score

    def prune_alpha(self, score, alpha, beta):
        alpha = max(alpha, score)
        return beta >= alpha

    def prune_beta(self, score, alpha, beta):
        beta = min(beta, score)
        return alpha >= beta

    def score_move(self, result):
        maximizer_token = self.processor.get_player_tokens()[self.maximizer_index]
        if result == maximizer_token:
            return 10
        elif result == constants.CATS:
            return 0
        else:
            return -10
