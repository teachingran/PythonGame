from commons import  General, Player
import numpy as np

def test():
    print('hi 2')
    current_board = '---------'
    while (True):
#        print_board (current_board)        
        row = int(input("pick row :from 1 to 3\n"))-1
        col = int(input("pick col :from 1 to 3\n"))-1
        sign = General.get_sign(Player.RIVAL)
        index = row*3+col
        current_board = current_board[:index] + sign + current_board[index+1:]
        print(f"current_board: {current_board}")
        np_array = np.array(list(current_board)).reshape(3, 3)
        print_board (np_array)


def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i, j], end=" ")
        print()

print('hi')
test()

    
    

