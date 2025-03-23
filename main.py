import numpy as np
from Game import Game
#import Tournement


def play_game():
    game= Game()
    game.play()
    aaa = game.get_game_result()
    print(aaa)
    np.save("res.txt")



if __name__ == '__main__':
    play_game()

