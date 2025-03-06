import random
import numpy as np


class Game:
    def __init__(self):
        self.board =np.array([[0,0,0],[0,0,0],[0,0,0]])
        self.free=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        self.print_board()

    def check_win(self):
        if self.board[0,0]==self.board[0,1] and self.board[0,0]==self.board[0,2]and self.board[0,0]!=0:
            return self.board[0,0]
        if self.board[1,0]==self.board[1,1] and self.board[1,0]==self.board[1,2]and self.board[1,0]!=0:
            return self.board[1,0]
        if self.board[2,0]==self.board[2,1] and self.board[2,0]==self.board[2,2]and self.board[2,0]!=0:
            return self.board[2,0]
        if self.board[0,0]==self.board[1,0] and self.board[0,0]==self.board[2,0]and self.board[0,0]!=0:
            return self.board[0,0]
        if self.board[0,1]==self.board[1,1] and self.board[0,1]==self.board[2,1]and self.board[0,1]!=0:
            return self.board[0,1]
        if self.board[0,2]==self.board[1,2] and self.board[0,2]==self.board[2,2]and self.board[0,0]!=0:
            return self.board[0,2]
        if self.board[0,0]==self.board[1,1] and self.board[0,0]==self.board[2,2]and self.board[0,0]!=0:
            return self.board[0,0]
        if self.board[2,0]==self.board[1,1] and self.board[2,0]==self.board[0,2]and self.board[2,0]!=0:
            return self.board[0,0]
        if len(self.free)==0:
            return 2

        return 0

    def perform_random_agent_move(self):
        place=random.randint(0,len(self.free)-1)
        self.board[self.free[place][0],self.free[place][1]]=1
        del self.free[place]

    def perform_random_rival_move(self):
        place=random.randint(0,len(self.free)-1)
        self.board[self.free[place][0],self.free[place][1]]=-1
        del self.free[place]

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i,j],end=" ")
            print()
        print()


    def play(self):
        stop=False
        while not stop:
            self.perform_random_agent_move()
            self.print_board()
            if self.check_win()!=0:
                stop=True
                break
            self.perform_random_rival_move()
            self.print_board()
            if self.check_win()!=0:
                stop=True
                break
        self.print_game_result()

    def print_game_result(self):
        win = self.check_win()
        if win == 1:
            print("Agent wins")
        elif win == -1:
            print("Rival wins")
        else:
            print("Tie")




