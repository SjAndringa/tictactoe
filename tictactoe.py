"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nX=0
    nO=0
    for i in range(3):
        for j in range(3):
            cell=board[i][j]
            if cell==X:
                nX += 1
            elif cell==O:
                nO += 1
    return X if nX <= nO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible=set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible.add((i,j))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard=deepcopy(board)
    newboard[action[0]][action[1]]=player(board)
    #print(newboard)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    """
    if player(board)==X:
        w=O
    else:
        w=X
    print("kijken of deze speler winnaar is ",w)
    """
    
    #rows
    for i in range(3):
        if allthree(board[i][0],board[i][1],board[i][2]):
            return board[i][0]
    #columns
    for i in range(3):
        if allthree(board[0][i],board[1][i],board[2][i]):
            return board[0][i]
    #diagonals
    if allthree(board[0][0],board[1][1],board[2][2]):
        return board[0][0]
    if allthree(board[2][0],board[1][1],board[0][2]):
        return board[2][0]
                    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) in [X,O]:
        #print("goed gespeeld door: ",dezewinnaar)
        return True
    elif bordvol(board):
        return True
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    dezewinnaar=winner(board)
    if dezewinnaar==X:
        return 1
    elif dezewinnaar==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return
    if player(board)==X:
        w=max_value(board)
    else:
        w=min_value(board)
    return w[0]
        
def max_value(board):
    #returns [move,value] that maximizes score
    v=-100
    w=[]
    if terminal(board):
        #print("max_value returns ",utility(board))
        
        return [w,utility(board)]
    for action in actions(board):
        temp=min_value(result(board,action))
        if temp[1]>v:
            v=temp[1]
            w=[action,temp[1]]
        # je moet ook nog de action erbij geven
    return w

def min_value(board):
    v=100
    if terminal(board):
        #print("min_value returns ",utility(board))
        return [None,utility(board)]
    for action in actions(board):
        temp=max_value(result(board,action))
        if temp[1]<v:
            v=temp[1]
            w=[action,temp[1]]
        # je moet ook nog de action erbij geven
    return w

def deepcopy(board):
    import copy
    return copy.deepcopy(board)

def allthree(a,b,c):
    return (a==b and b==c and a in [X,O])

def bordvol(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]is EMPTY:
                return False
    return True
