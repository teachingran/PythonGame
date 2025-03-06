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


test = Test()
test.tpl()
for i in range(100):
    test.random()