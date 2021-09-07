"""
This is board Game stimulation
There are min 2 and max n no of players.
Each player has to roll the dice to reach the target.
The player who reach the target first wins.
"""

from game import Game  # In PyCharm, mark parent directory as Sources Root for imports to work

if __name__ == '__main__':
    # game = Game(num_players=3, target_score=20)
    # game2 = Game(num_players=2, target_score=110)
    game2 = Game(num_players=2)

    # game.run()
    game2.run()
