import random
import numpy as np
from commons import GameStatus, Player

class Game:
    def __init__(self):
        self.board = np.array([[0,0,0], [0,0,0], [0,0,0]])
        self.not_used = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.game_status = GameStatus.KEEP_PLAYING

    def play(self):
        agent_turn = True
        while True:
#            self.print_board()
            if agent_turn:
                self.perform_agent_random_move()
            else:
                self.perform_rival_random_move()
            self.game_status = self.check_win()
#            self.print_game_result()
            if self.game_status == GameStatus.KEEP_PLAYING:
                agent_turn = not agent_turn
            else:
                break

                


    def __random_single_move(self, player):
        index = random.randint(0, len(self.not_used) - 1)
        tpl = self.not_used[index]
        del (self.not_used[index])
        self.board[tpl[0], tpl[1]] = player

    def perform_agent_random_move(self):
        self.__random_single_move(Player.AGENT)

    def perform_rival_random_move(self):
        self.__random_single_move(Player.RIVAL)

    def check_win(self):
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

    def print_game_result(self):
        if self.game_status == GameStatus.AGENT_WON:
            print("Agent wins")
        elif self.game_status == GameStatus.RIVAL_WON:
            print("Rival wins")
        else:
            print("Tie")


    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i, j], end=" ")
            print()

    # function is called after game is finished!!!
    # return 1d array: 
    #   first index is game's result
    #   other 9 indeces are the board's status
    def get_game_result(self):
        return np.append(self.game_status, self.board.reshape(9))
