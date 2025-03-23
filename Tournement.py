#from Game import Game
from NaiveGameForTraining import NaiveGameForTraining
from commons import GameStatus, General
import numpy as np
import os
import statistics
import pickle



class Tournament:
    def __init__(self):
        pass

    def play(self):
        print("start tournament")
        path = os.path.dirname(os.path.abspath(__file__))
        print(path)
        all_boards = {}
#        all_games = np.zeros((0,10), dtype=int)
        for i in range(1000000):
#            game = NaiveGameForTraining()
            game = NaiveGameForTraining()
            game.play()
            self.add_game_borads(game, all_boards)        

        #self.print_debug1(all_boards)
        self.calc_board_avg(all_boards)
        self.print_debug2(all_boards)
        self.save_results(all_boards)
        print("✔️'")       

    # instead of holding all scores concreteboard recieved, calc average and set it to concrete board
    def calc_board_avg(self, all_boards):
        for key in all_boards:
            all_boards[key] =  statistics.mean(all_boards[key])
        
    def save_results(self, all_boards):
        file_name = General.get_trained_file_name()
        with open(file_name, "wb") as file:
            pickle.dump(all_boards, file)
        print(f"✔️ dictionary saved in {file_name}")


    def add_game_borads(self, game, all_boards):
        for board in game.grades_boards:
            if board[0] in all_boards:
                all_boards[board[0]].append(board[1])
            else:
                all_boards[board[0]] = [(board[1])]


        
    # see all ranks that were related to concrete board
    # ie  XOOXOXXOX: 0.81, 0.55, 0.81, 0.3, ...
    def print_debug1(self, all_boards):
        with open("data_debug1.txt", "w") as file:
            for key, values in all_boards   .items():
                file.write(f"{key}: {', '.join(map(str, values))}\n")
        print("✔️ file 'data_debug1.txt' generated")

    # see calculated rank related to concrete board
    # ie  XOOXOXXOX: 0.632
    def print_debug2(self, all_boards):
        import csv
        with open("data_debug2.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Key", "Value"])
            for key, value in all_boards.items():
                writer.writerow([key, value])
        print("✔️ המידע נשמר כ-CSV בקובץ 'data_debug2.csv'")       



    def get_file_path(self):
        path = os.path.dirname(os.path.abspath(__file__))
        return path + r'\res.txt'

tournament = Tournament()
tournament.play()