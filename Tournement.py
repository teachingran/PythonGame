from Game import Game
import numpy as np
import os

class Tournament:
    def __init__(self):
        pass




    def play(self):
        path = os.path.dirname(os.path.abspath(__file__))
        print(path)

        all_games = np.zeros((0,10), dtype=int)
        for i in range(1000):
            game = Game()
            game.play()
            game_status = game.get_game_result()
            all_games = np.append(all_games, [game_status], axis=0)
            print(all_games)


        file_name = self.get_file_path()
        np.savetxt (file_name, all_games, fmt='%d')

    def get_file_path(self):
        path = os.path.dirname(os.path.abspath(__file__))
        return path + r'\res.txt'

tournament = Tournament()
tournament.play()