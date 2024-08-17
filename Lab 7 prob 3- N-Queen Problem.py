# Implement N-Queen Problem in Constraint Satisfaction Problem.

def is_valid(board, row, col):
    for i in range(row):
        # Check column and diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_csp(board, row):
    n = len(board)
    if row >= n:
        return True
    
    # Skip rows where queens are already placed
    if board[row] != -1:
        return solve_n_queens_csp(board, row + 1)

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            if solve_n_queens_csp(board, row + 1):
                return True
            board[row] = -1  # Backtrack
    
    return False

def print_board(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Initialize board with fixed queens
n = 4
board = [-1] * n  # -1 indicates no queen placed
board[0] = 1  # Q at (0, 1)
board[1] = 3  # Q at (1, 3)
board[2] = 0  # Q at (2, 0)
board[3] = 2  # Q at (3, 2)

# Solve the N-Queens problem with fixed queens
if solve_n_queens_csp(board, 0):
    print("Solution found:")
    print_board(board)
else:
    print("No solution exists.")

