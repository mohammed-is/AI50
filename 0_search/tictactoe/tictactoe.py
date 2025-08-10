"""
Tic Tac Toe Player
"""

import copy
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
    count_x = 0
    count_o = 0
    for row in board:
        for col in row:
            if col == X:
                count_x += 1
            if col == O:
                count_o += 1

    if count_o == count_x:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action

    # validation
    assert row in (0, 1, 2) and col in (0, 1, 2), "invalid action position"
    if board[row][col] != EMPTY:
        raise Exception("position not empty")

    # apply the turn in a copy if the board
    turn = player(board)
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = turn

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # three in a row
        char = board[i][0]
        if char and char == board[i][1] and char == board[i][2]:
            return char

        # three in a column
        char = board[0][i]
        if char and char == board[1][i] and char == board[2][i]:
            return char

    # three diagonal
    if board[1][1] and (
        (board[0][0] == board[1][1] == board[2][2]) 
        or
        (board[0][2] == board[1][1] == board[2][0])
    ):
        return board[1][1]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for row in board:
            for col in row:
                if col == EMPTY:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return {X: 1, O: -1, None: 0}[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        max_v = -math.inf
        max_action = None
        for action in actions(board):
            v = min_value(result(board, action), -math.inf, math.inf)
            if v > max_v:
                max_v = v
                max_action = action
        return max_action
    else:
        min_v = math.inf
        min_action = None
        for action in actions(board):
            v = max_value(result(board, action), -math.inf, math.inf)
            if v < min_v:
                min_v = v
                min_action = action
        return min_action



def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        new_board = result(board, action)
        v = min(v, max_value(new_board, alpha, beta))
        
        # stop if less than last min
        beta = min(v, beta)
        if beta <= alpha:
            break

    return v


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        new_board = result(board, action)
        v = max(v, min_value(new_board, alpha, beta))
        
        # stop if grater than last max
        alpha = max(v, alpha)
        if alpha >= beta:
            break

    return v
