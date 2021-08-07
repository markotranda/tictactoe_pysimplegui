import copy
from typing import Dict

class TicTacToe:
    states = {
        -1: 'O', 
        0: '.', 
        1: 'X'
    }

    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_player = -1
        self.current_state = [0 for _ in range(9)]

    def play(self, move: int) -> bool:
        if self.current_state[move] != 0:
            print('Morate izabrati prazno polje')
            return False
        else:
            self.current_player *= -1
            self.current_state[move] = self.current_player

    def evaluate(self) -> int:
        state = self.current_state
        winner = None
        if len([x for x in state if x == 0]) == 0:
            return 0
        elif 0 != state[0] == state[1] == state[2]:
            winner = state[0]
        elif 0 != state[3] == state[4] == state[5]:
            winner = state[3]
        elif 0 != state[6] == state[7] == state[8]:
            winner = state[6]
        elif 0 != state[0] == state[3] == state[6]:
            winner = state[0]
        elif 0 != state[1] == state[4] == state[7]:
            winner = state[1]
        elif 0 != state[2] == state[5] == state[8]:
            winner = state[2]
        elif 0 != state[0] == state[4] == state[8]:
            winner = state[0]
        elif 0 != state[2] == state[4] == state[6]:
            winner = state[2]
        
        if winner == None:
            return None
        elif winner == self.current_player:
            return 1
        else:
            return -1

    def is_over(self) -> bool:
        val = self.evaluate()
        if val == None:
            return False
        if self.evaluate() == 0:
            print('Nereseno je!')
            return True
        else:
            print(f'Pobednik je {self.states[self.current_player]}!')
            return True
    
    def copy_current_state(self) -> list:
        return copy.deepcopy(self.current_state)

    def get_current_player(self) -> int:
        return self.current_player * -1
    
    def __str__(self) -> str:
        board = [self.states[x] for x in self.current_state]
        board_print = ''
        board_print += f"{board[0]}|{board[1]}|{board[2]}\n"
        board_print += "-----\n"
        board_print += f"{board[3]}|{board[4]}|{board[5]}\n"
        board_print += "-----\n"
        board_print += f"{board[6]}|{board[7]}|{board[8]}\n"
        return board_print
    
    def get_state(self) -> list:
        return [self.states[x] for x in self.current_state]
        
    
