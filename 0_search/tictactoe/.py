import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    return X if count_x == count_o else O


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    row, col = action
    assert row in (0, 1, 2) and col in (0, 1, 2), "invalid action position"
    if board[row][col] != EMPTY:
        raise ValueError("Position not empty")

    new_board = copy.deepcopy(board)
    new_board[row][col] = player(board)
    return new_board


def winner(board):
    # Rows & columns
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # Diagonals
    if board[1][1] and (
        (board[0][0] == board[1][1] == board[2][2]) or
        (board[0][2] == board[1][1] == board[2][0])
    ):
        return board[1][1]

    return None


def terminal(board):
    return winner(board) is not None or all(col is not EMPTY for row in board for col in row)


def utility(board):
    w = winner(board)
    return 1 if w == X else -1 if w == O else 0


def minimax(board):
    if terminal(board):
        return None

    turn = player(board)
    if turn == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action), -math.inf, math.inf)
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action), -math.inf, math.inf)
            if score < best_score:
                best_score = score
                best_action = action
        return best_action


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break  # Beta cut-off
    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if alpha >= beta:
            break  # Alpha cut-off
    return v
