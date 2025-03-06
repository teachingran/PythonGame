from Game import Game
import random
import numpy as np
from commons import GameStatus

class Test:
    def __init__(self):
        self.board = np.array([[0,0,0], [0,0,0], [0,0,0]])
        self.not_used = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.index = 1

    def print(self, msg):
        print (self.index,"->", msg)
        self.index += 1

    def tpl(self):
        index = tuple([2,1])
        index = (2,1)
        self.print(str(index[0]) + str(index[1]))
        self.print(self.board[2,1])
        self.print(self.board[index[0],index[1]])
        self.board[2,1] = 1
        print("ggg")
        row = index[0]
        col = index[1]
        self.board[row, col] = 1

    def random(self):
        index = random.randint(0, len(self.not_used) - 1)
        print(index)

    def np_add(self):
        # Create a 2D numpy array
        array_2d = np.array([[1, 2, 3], [4, 5, 6]])

        # Create a 1D numpy array
        array_1d = np.array([7, 8, 9])

        # Add the 1D array as a new row
        array_2d = np.append(array_2d, [array_1d], axis=0)
        import pathlib
        path = pathlib.Path().resolve()
        print(path)

        import os
        path = os.path.dirname(os.path.abspath(__file__))
        print(path)
        np.savetxt(path+r'\res.txt', array_2d, fmt='%d')

        print(array_2d)

    def np_res(self):
        game= Game()
        game.play()
        aaa = game.get_game_result()
        print(type(aaa))
        print(aaa)
#        np.save()




test = Test()
test.np_res()
#test.np_add()
#test.tpl()
#for i in range(100):
#    test.random()