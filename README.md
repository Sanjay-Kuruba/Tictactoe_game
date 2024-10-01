# Tictactoe_game
Run file Runner.py to execute gameplay with computer
Functions used in Tictactoe.py and logic behind implementation.
1. player(board)
Count how many X and O symbols are already on the board.
If X has made more moves, return O (since it alternates), otherwise return X.
2. actions(board)
The function loops through the entire 3x3 board and checks if each cell is 
EMPTY. If a cell is empty, it adds its coordinates to a set of possible actions.
3.result(board, action)
First, it checks if the chosen action is valid (i.e., if the cell is empty).
If valid, it creates a copy of the current board and updates the specified position with the current 
player's symbol (X or O).
The new board state is returned without modifying the original board.
4.winner(board)
It first checks each row and each column to see if all three cells are occupied by the same player (X or O).
Then, it checks the two diagonals for the same condition.
If a winning condition is found, it returns the winner (X or O); otherwise, it returns None.
5.terminal(board)
First, it checks if there is a winner by calling the winner() function.
If there's no winner, it checks whether all the cells on the board are filled (i.e., no empty spaces).
If either condition is true, the game is over, and the function returns True; otherwise, it returns False.
6.utility(board)
It first checks if there is a winner using the winner() function.
Depending on the result, it returns the appropriate score for the game outcome (1, -1, or 0).
7.minimax(board)
If the game is over (terminal(board) returns True), there are no possible moves left.
Otherwise, it calls max_value() or min_value() depending on whose turn it is, selecting the optimal move for that player.
8.max_value(board)
If the game is over, it returns the utility of the current board state.
Otherwise, it iterates over all possible actions and simulates the outcome of each move using result().
It calls min_value() to evaluate each outcome and selects the move that maximizes the score.
The function returns the highest utility and the corresponding action.
9.min_value(board)
Like max_value(), it first checks if the game is over and returns the utility if so.
Otherwise, it evaluates all possible moves using max_value() and selects the one that minimizes the score for O.
