import copy
import random
import numpy as np

class AI:
    def __init__(self, player: int) -> None:
        self.player = player
    
    def evaluate(self, state: list) -> int:
        winner = None
        if len([x for x in state if x == 0]) == 0:
            return 0
        if 0 != state[0] == state[1] == state[2]:
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
        elif winner == self.player:
            return 1
        else:
            return -1

    def get_possible_moves(self, state: list) -> list:
        return [x for x in range(len(state)) if state[x] == 0]
    
    def new_state(self, state: list, move: int, player: int):
        new_state = copy.deepcopy(state)
        new_state[move] = player
        return new_state

    def pick_move(self, state_copy: list) -> int:
        move = self.minimax(state_copy)
        print(move)
        return move

    def minimax(self, state: list) -> int:
        # !!!!! (score, move) !!!!!
        return self._max(state, None, float('-inf'), float('inf'))[1]

    def _max(self, state: list, move: int, alfa, beta) -> tuple:
        val = self.evaluate(state)
        if val != None:
            return (val, move)
        # scores = [(self._min(self.new_state(state, _move, self.player), _move)[0], _move) for _move in self.get_possible_moves(state)]
        best_score = (float('-inf'), None)
        for _move in self.get_possible_moves(state):
            new_score = (self._min(self.new_state(state, _move, self.player), _move, alfa, beta)[0], _move)
            if new_score[0] > alfa:
                alfa = new_score[0]
            if new_score[0] >= beta:
                return new_score
            if new_score > best_score:
                best_score = new_score
        return best_score

    def _min(self, state: list, move: int, alfa, beta) -> tuple:
        val = self.evaluate(state)
        if val != None:
            return (val, move)
        # scores = [(self._max(self.new_state(state, _move, self.player * -1), _move)[0], _move) for _move in self.get_possible_moves(state)]
        best_score = (float('inf'), None)
        for _move in self.get_possible_moves(state):
            new_score = (self._max(self.new_state(state, _move, self.player), _move, alfa, beta)[0], _move)
            if new_score[0] < beta:
                alfa = new_score[0]
            if new_score[0] <= alfa:
                return new_score
            if new_score < best_score:
                best_score = new_score
        return best_score
    
