#!/usr/bin/env python3
''' Tic-Tac-Toe Minimax Program by Peter'''
#Tutorial found at: http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html'''
class GameState:
    def __init__(self,board,char='X',oppchar='O'):
        self.char = char
        self.oppchar = oppchar
        self.board = board
        self.winning_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def is_gameover(self):
        '''returns if a game_state has been won or filled up'''
        if self.board.count(self.char) + self.board.count(self.oppchar) == 9:
            return True
        for combo in self.winning_combos:
            if (self.board[combo[0]] == self.char and self.board[combo[1]] == self.char and self.board[combo[2]] == self.char) or \
            (self.board[combo[0]] == self.oppchar and self.board[combo[1]] == self.oppchar and self.board[combo[2]] == self.oppchar):
                return True
        return False

    @staticmethod
    def return_state(score):
        if score == 0:
            return('TIED')
        elif score == 1:
            return('WON')
        elif score == -1:
            return('LOST')
        else:
            return('ERROR')

    def pretty_print(self):
        '''prints a list by 3 chars, joined by spaces'''
        print(' '.join(self.board[:3]))
        print(' '.join(self.board[3:6]))
        print(' '.join(self.board[6:9]))

    def get_possible_moves(self):
        '''returns all possible squares to place a character'''
        squares = []
        for index, square in enumerate(self.board):
            if square != self.char and square != self.oppchar:
                squares.append(index)
        return squares

    def get_next_state(self, move, our_turn):
        '''returns the gamestate with the move filled in'''
        copy = self.board[:]
        if our_turn:
            copy[move] = self.char
        else:
            copy[move] = self.oppchar
        return GameState(copy, char=self.char, oppchar=self.oppchar)

    def score(self):
        '''score a game_state from the computers point of view, 1 = win, 0 = tie, -1 = lose'''
        for combo in self.winning_combos:
            if self.board[combo[0]] == self.char and self.board[combo[1]] == self.char and self.board[combo[2]] == self.char:
                return 1    
            elif self.board[combo[0]] == self.oppchar and self.board[combo[1]] == self.oppchar and self.board[combo[2]] == self.oppchar:
                return -1
        return 0

'''max and min will call on each other recusively, until a terminal state'''
def max_play(game_state):
    '''if the game is over returns score, otherwise calls min_play on it's childen (possible moves from the state) and returns the maximum'''
    if game_state.is_gameover():
        return game_state.score()
    return max(map(lambda move: min_play(game_state.get_next_state(move, True)), game_state.get_possible_moves()))

def min_play(game_state):
    '''if the game is over returns score, otherwise calls max_play on it's childen (possible moves from the state) and returns the minimum'''
    if game_state.is_gameover():
        return game_state.score()
    return min(map(lambda move: max_play(game_state.get_next_state(move, False)), game_state.get_possible_moves()))

def minimax(game_state):
    '''returns the max of mapping the (move, score) tuple to the possible move using [1] of the tuple the (score)'''
    return max(map(lambda move: (move, min_play(game_state.get_next_state(move, True))), game_state.get_possible_moves()), key = lambda x: x[1])