import src.constants as constants

class Processor():
    def __init__(self, board):
        self.board = board
        self.set_win_combos()

    def set_win_combos(self):
        print(self.board.type)
        if self.board.type == constants.THREE_BY_THREE:
            self.win_combos = constants.THREE_BY_THREE_WIN_COMBINATIONS
        elif self.board.type == constants.THREE_DIMENSIONAL:
            self.win_combos = constants.THREE_DIMENSIONAL_WIN_COMBINATIONS

    def set_players(self, players):
        self.players = players

    def move_to_index(self, move):
        return int(move) - 1

    def get_valid_moves(self):
        return [index + 1 for index, space in enumerate(self.board.spaces) if space == None]

    def get_taken_positions(self):
        return [index for index, space in enumerate(self.board.spaces) if space != None]

    def valid_move(self, move):
        position = self.move_to_index(move)
        return self.board.within_board(position) and not self.board.position_taken(position)

    def execute_move(self, move, token):
        index = self.move_to_index(move)
        self.board.update(index, token)
        return self.move_result()

    def move_result(self):
        winner = self.winner()
        if winner: return winner
        elif self.cats_game(): return constants.CATS 

    def cats_game(self):
        return self.board.full() and not self.winner()

    def get_player_tokens(self):
        return [player.token for player in self.players]

    def current_player(self):
        num_players = len(self.players)
        turns_taken = self.board.turn_count()
        return self.players[turns_taken % num_players]

    def next_player_index(self, current_player_index):
        num_players = len(self.players)
        if current_player_index == num_players - 1:
            return 0 
        else:
            return current_player_index + 1

    def generate_move_action(self, move):
        if move == constants.EXIT:
            return [constants.EXIT, None]
        elif self.valid_move(move):
            return [constants.MOVE, move]
        
        return [constants.ERROR, move]

    def compare_board_indicies(self, index_1, index_2):
        return self.board.token_at(index_1) == self.board.token_at(index_2)

    def check_combo(self, combo):
        indices = range(len(combo) - 1)
        is_equal = True
        for index in indices:
            if not self.compare_board_indicies(combo[index], combo[index + 1]):
                is_equal = False
        return is_equal

    def winner(self):
        winner = None
        for combo in self.win_combos.values():
            if self.check_combo(combo) and self.board.position_taken(combo[0]):
                winner = self.board.token_at(combo[0])
                break;

        return winner

