import numpy as np
import random
from colorama import init, Fore, Style
from tkinter import *
import game



# Define the Minimax algorithm
def minimax(board, depth, maximizingPlayer):
    # Check for terminal node or maximum depth
    score = game.evaluate(board)
    if abs(score) == 100 or depth == 0:
        return score, None
    # Initialize best score and best move
    if maximizingPlayer:
        bestScore = -np.inf
        for col in range(7):
            # Check for valid move
            if board[0][col] == 0:
                # Make move and recurse
                row = 5
                while row >= 0 and board[row][col] != 0:
                    row -= 1
                board[row][col] = 1
                childScore, _ = minimax(board, depth - 1, False)
                board[row][col] = 0
                # Update best score and best move
                if childScore > bestScore:
                    bestScore = childScore
                    bestMove = col

    else:
        bestScore = np.inf
        for col in range(7):
            # Check for valid move
            if board[0][col] == 0:
                # Make move and recurse
                row = 5
                while row >= 0 and board[row][col] != 0:
                    row -= 1
                board[row][col] = 2
                childScore, _ = minimax(board, depth - 1, True)
                board[row][col] = 0
                # Update best score and best move
                if childScore < bestScore:
                    bestScore = childScore
                    bestMove = col

    return bestScore, bestMove