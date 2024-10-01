import math# Import the math module

X = "X"
O = "O"
EMPTY = None
# Function to create the initial game state (an empty 3x3 board)
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
# Function to determine whose turn it is based on the current game state
def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O
# Function to get all possible actions (empty cells) on the current game state
def actions(board):
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions
# Function to get the resulting game state after taking a specific action
def result(board, action):
    new_board = [row.copy() for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board
# Function to check if there is a winner on the current game state
def winner(board):
    for i in range(3):    # Check rows for a winner
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None
# Function to check if the game is terminal (won or drawn)
def terminal(board):
    if winner(board) is not None:# If there is a winner, the game is terminal
        return True
    for row in board:
        if EMPTY in row:    # If there are no more empty cells, the game is a draw
            return False
    return True
# Function to calculate the utility of the game state (1 for X win, -1 for O win, 0 for draw)
def utility(board):
    winner_val = winner(board)
    if winner_val == X:   # If X has won the game, return 1
        return 1
    elif winner_val == O:# If O has won the game, return -1
        return -1
    else:#If the game has ended in a tie,
        return 0
# Minimax algorithm to determine the best move for the current player
def minimax(board):
    if terminal(board):# If game is over, return None
        return None
    if player(board) == X:# X's turn: find best move that maximizes utility
        best_val = -math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            val = minimax_helper(new_board, -math.inf, math.inf)
            if val > best_val:
                best_val = val
                best_action = action
        return best_action
    else:
        best_val = math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            val = minimax_helper(new_board, -math.inf, math.inf)
            if val < best_val:
                best_val = val
                best_action = action
        return best_action
# Recursive helper function to evaluate game state and return best value
def minimax_helper(board, alpha, beta):
    if terminal(board):# If game is over, return utility of board
        return utility(board)
    if player(board) == X:# X's turn: find best move that maximizes utility
        best_val = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            val = minimax_helper(new_board, alpha, beta)
            best_val = max(best_val, val)
            alpha = max(alpha, val)
            if beta <= alpha: # Prune search tree if beta <= alpha
                break
        return best_val
    else: # O's turn: find best move that minimizes utility
        best_val = math.inf
        for action in actions(board):
            new_board = result(board, action)
            val = minimax_helper(new_board, alpha, beta)
            best_val = min(best_val, val)# Update best value and beta
            beta = min(beta, val)
            if beta <= alpha:# Prune search tree if beta <= alpha
                break
        return best_val