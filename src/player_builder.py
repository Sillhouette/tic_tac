from src.player import Player

class PlayerBuilder():
    def build_players(self, player_tokens):
        players = []
        for token in player_tokens:
            players.append(Player(token=token))

        return players


