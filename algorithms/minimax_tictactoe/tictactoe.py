"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_counter, o_counter = 0,0
    for row in range(3):
        for column in range(3):
            if board[row][column] == "X":
                x_counter+=1
            elif board[row][column] == "O":
                o_counter+=1
    if x_counter<=o_counter:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                all_actions.add((row, column))
    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not(0<=action[0]<3 and 0<=action[1]<3):
        raise Exception("Out of boundaries")
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")
    row_to_update, column_to_update = action
    new_board = copy.deepcopy(board)
    new_board[row_to_update][column_to_update]=player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return check_board(board)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if check_board(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    res = check_board(board)
    if res == "X":
        return 1
    elif res == "O":
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None  # нет доступных ходов

    current_player = player(board)

    if current_player == "X":
        best_score = float("-inf")
        best_action = None

        for action in actions(board):
            new_board = result(board, action)
            score = min_value(new_board)
            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    else:  # current_player == "O"
        best_score = float("inf")
        best_action = None

        for action in actions(board):
            new_board = result(board, action)
            score = max_value(new_board)
            if score < best_score:
                best_score = score
                best_action = action

        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def check_board(board):
    combinations_to_win = ([[0, 0], [0, 1], [0, 2]],
                           [[1, 0], [1, 1], [1, 2]],
                           [[2, 0], [2, 1], [2, 2]],
                           [[0, 0], [1, 0], [2, 0]],
                           [[0, 1], [1, 1], [2, 1]],
                           [[0, 2], [1, 2], [2, 2]],
                           [[0, 0], [1, 1], [2, 2]],
                           [[2, 0], [1, 1], [0, 2]]
                           )
    for combination in combinations_to_win:
        x_counter = 0
        o_counter = 0
        for row, column in combination:
            cell = board[row][column]
            if cell == "X":
                x_counter += 1
            elif cell == "O":
                o_counter += 1
            if x_counter == 3:
                return "X"
            if o_counter == 3:
                return "O"
    return None

