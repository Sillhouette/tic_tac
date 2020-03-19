import src.constants as constants
import math

class Minimax():
    def __init__(self, processor, maximizer_index):
        self.processor = processor 
        self.maximizer_index = maximizer_index

    def execute(self, move, depth, token, next_player_index,
                   alpha=-math.inf, beta=math.inf):
        self.processor.execute_move(move, token)
        score = self.score_move(depth, next_player_index, alpha, beta)
        self.processor.execute_move(move, None)

        return score
    
    def calculate_score(self, result):
        maximizer_token = self.processor.get_player_tokens()[self.maximizer_index]
        if result == maximizer_token:
            return 10
        elif result == constants.CATS:
            return 0
        else:
            return -10

    def score_move(self, depth, player_index, alpha, beta):
        result = self.processor.move_result()
        if result != None:
            return self.calculate_score(result)

        if player_index == self.maximizer_index:
            best_score = -math.inf
            min_max = max
            prune = self.prune_alpha
        else:
            best_score = math.inf
            min_max = min 
            prune = self.prune_beta

        return self.calculate_best_score(depth, player_index, alpha, beta, best_score,
                                 prune, min_max)

    def calculate_best_score(self, depth, player_index, alpha,
                             beta, best_score, prune, min_max):
        token = self.processor.get_player_tokens()[player_index]
        next_player_index = self.processor.next_player_index(player_index)
        for move in self.processor.get_valid_moves():
            score = self.execute(move, depth + 1, token,  next_player_index, alpha, beta)
            best_score = min_max(score, best_score)
            if prune(best_score, alpha, beta):
                pass
        return best_score

    def prune_alpha(self, score, alpha, beta):
        alpha = max(alpha, score)
        return beta >= alpha

    def prune_beta(self, score, alpha, beta):
        beta = min(beta, score)
        return alpha >= beta

