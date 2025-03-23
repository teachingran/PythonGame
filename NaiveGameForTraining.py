from BaseGame import BaseGame
from commons import GameStatus, Player, General

import os
import random
import numpy as np


class NaiveGameForTraining(BaseGame):
    def __init__(self):
        super().__init__()

    def perform_agent_move(self):
        self.random_single_move(Player.AGENT)


    def perform_rival_move(self):
        self.random_single_move(Player.RIVAL)

    def random_single_move(self, player):
        index = random.randint(0, len(self.not_used) - 1)
        tpl = self.not_used[index]
        del (self.not_used[index])
        self.add_current_board(tpl[0],tpl[1], player)
        self.board[tpl[0], tpl[1]] = player

    def add_current_board(self, row, col, player):
        sign = General.get_sign(player)
        index = row*3+col
        self.current_board = self.current_board[:index] + sign + self.current_board[index+1:]
        self.list_of_boards.append(self.current_board)
 #       print(self.current_board)

    # override
    def end_game(self):
        self.build_grades()

    def build_grades(self):
        self.list_of_boards.reverse()
        rank, gamma = General.get_gamma(self.game_status)

        for board in self.list_of_boards:
            self.grades_boards.append((board, rank))
            rank *= gamma


    def check_win(self):
#        self.print_board()
        if not self.not_used:
            return GameStatus.TIE
        if self.board[0, 0] == self.board[0, 1] and self.board[0, 0] == self.board[0, 2] and self.board[0, 0] != 0:
            return self.board[0, 0]
        elif self.board[1, 0] == self.board[1, 1] and self.board[1, 0] == self.board[1, 2] and self.board[1, 0] != 0:
            return self.board[1, 0]
        elif self.board[2, 0] == self.board[2, 1] and self.board[2, 0] == self.board[2, 2] and self.board[2, 0] != 0:
            return self.board[2, 0]
        elif self.board[0, 0] == self.board[1, 0] and self.board[0, 0] == self.board[2, 0] and self.board[0, 0] != 0:
            return self.board[0, 0]
        elif self.board[0, 1] == self.board[1, 1] and self.board[0, 1] == self.board[2, 1] and self.board[0, 1] != 0:
            return self.board[0, 1]
        elif self.board[0, 2] == self.board[1, 2] and self.board[0, 2] == self.board[2, 2] and self.board[0, 2] != 0:
            return self.board[0, 2]
        elif self.board[0, 0] == self.board[1, 1] and self.board[0, 0] == self.board[2, 2] and self.board[0, 0] != 0:
            return self.board[0, 0]
        elif self.board[2, 0] == self.board[1, 1] and self.board[2, 0] == self.board[0, 2] and self.board[2, 0] != 0:
            return self.board[2, 0]
        return GameStatus.KEEP_PLAYING


    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i, j], end=" ")
            print()
