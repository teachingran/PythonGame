import os
import random
import numpy as np
from commons import GameStatus, General
from abc import ABC, abstractmethod


class BaseGame():
    def __init__(self):
        self.board = np.array([[0,0,0], [0,0,0], [0,0,0]])
        self.not_used = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.game_status = GameStatus.KEEP_PLAYING
        self.list_of_boards = []
        self.grades_boards = []
        self.current_board = "---------"

    def play(self):
        agent_turn = True
        while True: #self.game_status == GameStatus.KEEP_PLAYING:
#            self.print_board()
            if agent_turn:
                self.perform_agent_move()
            else:
                self.perform_rival_move()
            self.game_status = self.check_win()

#            self.print_game_result()
            if self.game_status == GameStatus.KEEP_PLAYING:
                agent_turn = not agent_turn
            else:
                self.end_game()
                break



    @abstractmethod
    def end_game(self):
        pass


    @abstractmethod
    def perform_agent_move(self):
        pass


    @abstractmethod
    def perform_rival_move(self):
        pass

    @abstractmethod
    def check_win(self):
        pass



    @abstractmethod
    def print_board(self):
        pass


    # function is called after game is finished!!!
    # return 1d array: 
    #   first index is game's result
    #   other 9 indeces are the board's status
#    def get_game_result(self):
#        return np.append(self.game_status, self.board.reshape(9))


def test():


    game = BaseGame()
    game.play()
 #   game_status = game.get_game_result()


#test()
#        all_games = np.append(all_games, [game_status], axis=0)
 #       print(all_games)
