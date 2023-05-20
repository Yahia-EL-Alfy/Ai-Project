

# Define the evaluation function for the board state
def evaluate(board):
    # Check for horizontal wins
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                if board[row][col] == 1:
                    return 100
                elif board[row][col] == 2:
                    return -100
    # Check for vertical wins
    for row in range(3):
        for col in range(7):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                if board[row][col] == 1:
                    return 100
                elif board[row][col] == 2:
                    return -100
    # Check for diagonal wins (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                if board[row][col] == 1:
                    return 100
                elif board[row][col] == 2:
                    return -100
    # Check for diagonal wins (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                if board[row][col] == 1:
                    return 100
                elif board[row][col] == 2:
                    return -100
    # If no wins, return 0
    return 0