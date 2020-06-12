import src.constants as constants
import math

class Minimax():
    def __init__(self, processor, maximizer_index, max_depth=None, data_gatherer=None):
        self.processor = processor 
        self.maximizer_index = maximizer_index
        self.data_gatherer = data_gatherer
        self.max_depth = max_depth

    def calculate_score(self, result):
        maximizer_token = self.processor.get_player_tokens()[self.maximizer_index]
        if result == maximizer_token:
            return 10
        elif result == constants.CATS:
            return 0
        else:
            return -10

    def get_best_move(self, depth, player_index, best_move=None, alpha=-math.inf, beta=math.inf):
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

        token = self.processor.get_player_tokens()[player_index]
        next_player_index = self.processor.next_player_index(player_index)
        valid_moves = self.processor.get_valid_moves()
        for move in valid_moves:
            if self.max_depth and depth == self.max_depth:
                return best_score

            self.processor.execute_move(move, token)
            score = self.get_best_move(depth + 1, next_player_index, best_move, alpha, beta)
            self.processor.execute_move(move, None)

            best_score = min_max(score, best_score)
            if best_score == score:
                best_move = move
            
            if prune(best_score, alpha, beta):
                pass
        
        if self.data_gatherer:
            three_dimensional = self.processor.board.type == constants.THREE_DIMENSIONAL
            self.data_gatherer.store_result(self.processor.board.spaces, best_move, three_dimensional)
        
        if depth == 0:
            return best_move
        return best_score

    def prune_alpha(self, score, alpha, beta):
        alpha = max(alpha, score)
        return beta >= alpha

    def prune_beta(self, score, alpha, beta):
        beta = min(beta, score)
        return alpha >= beta

