from BaseGame import BaseGame
from commons import GameStatus, Player, General
import numpy as np
import pickle


class BotGame(BaseGame):
    def __init__(self):
        super().__init__()
        self.graded_boards = self.load_results()


    def load_results(self):
        file_name = General.get_trained_file_name()
        with open(file_name, 'rb') as file:
            return pickle.load(file)
        

    def perform_agent_move(self):
        self.current_board = self.pick_best_move()

    
    def perform_rival_move(self):
        row = int(input("pick row :from 1 to 3\n"))-1
        col = int(input("pick col :from 1 to 3\n"))-1
        sign = General.get_sign(Player.RIVAL)
        index = row*3+col
        self.current_board = self.current_board[:index] + sign + self.current_board[index+1:]
        self.list_of_boards.append(self.current_board)



    def pick_best_move(self):
        print(self.current_board)
        moves = {}
        new_move ="" #will be some default if no suggestion made
        for i, char in enumerate(self.current_board):
            if char == '-':
                new_move = self.current_board[:i] + 'X' + self.current_board[i+1:]  # Replace '-' with 'X'
                if new_move in self.graded_boards:
                    moves[new_move] = self.graded_boards[new_move]
        if len(moves) == 0:
            return new_move
        
        best_key = max(moves, key=moves.get)
        print(f"move grade is {moves[best_key]}")
        return best_key

    # override
    def end_game(self):
        self.print_game_result()
        

    def print_game_result(self):
        if self.game_status == GameStatus.AGENT_WON:
            print("Agent wins")
        elif self.game_status == GameStatus.RIVAL_WON:
            print("Rival wins")
        else:
            print("Tie")

    def check_win(self):
        self.print_board()
        # Winning combinations (row-wise, column-wise, diagonal-wise)
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        
        # Check for a winner
        for a, b, c in winning_combinations:
            if self.current_board[a] == self.current_board[b] == self.current_board[c] and self.current_board[a] =='X':
                return GameStatus.AGENT_WON
            elif self.current_board[a] == self.current_board[b] == self.current_board[c] and self.current_board[a] =='O':
                return GameStatus.RIVAL_WON
        
        # Check for a tie (if there are no empty spots '-')
        if '-' not in self.current_board:
            return GameStatus.TIE
        
        return GameStatus.KEEP_PLAYING

    
    def print_board(self):
        np_array = np.array(list(self.current_board)).reshape(3, 3)
        for i in range(3):
            for j in range(3):
                print(np_array[i, j], end=" ")
            print()

def test():
    print('hi 2')
    current_board = '---------'
    while (True):
        row = int(input("pick row :from 1 to 3\n"))-1
        col = int(input("pick col :from 1 to 3\n"))-1
        sign = General.get_sign(Player.RIVAL)
        index = row*3+col
        current_board = current_board[:index] + sign + current_board[index+1:]
        np_array = np.array(list(current_board)).reshape(3, 3)
#        print_board (np_array)

def play_game():
    game = BotGame()
    game.play()

play_game()


#test()

    
    

