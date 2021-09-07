"""
How the game works
"""
from player import Player


class Game:
    """
    This in Game Class
    """
    def __init__(self, num_players, target_score=100):
        self.target_score = target_score
        self.players = [Player(i + 1) for i in range(num_players)]
        self._game_over = False
        self._winner = None

    def run_round(self):
        """
        Each player roll's the dice in their turn.
        """
        for player in self.players:
            player.take_turn()
            if self._player_has_won(player):
                self._winner = player
                self._game_over = True

    def _player_has_won(self, player):
        return player.score >= self.target_score

    def _game_start(self):
        print(f"Start game: {self}")

    def _game_end(self):
        print(f"{self._winner} wins!")
        print("-----------------")

    def run(self):
        """
        Runs until a player wins
        """
        self._game_start()
        while True:
            self.run_round()
            if self._game_over:
                self._game_end()
                return

    def __str__(self):
        return f"{len(self.players)}-player game to {self.target_score}"
