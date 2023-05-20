import numpy as np
import random
from colorama import init, Fore, Style
from tkinter import *
import game




# Define the Minimax algorithm with Alpha-Beta pruning
def minimax_alpha_beta(board, depth, alpha, beta, maximizingPlayer):
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
                childScore, _ = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
                board[row][col] = 0
                # Update best score and best move
                if childScore > bestScore:
                    bestScore = childScore
                    bestMove = col
                # Update alpha
                alpha = max(alpha, bestScore)
                if alpha >= beta:
                    break

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
                childScore, _ = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
                board[row][col] = 0
                # Update best score and best move
                if childScore < bestScore:
                    bestScore = childScore
                    bestMove = col
                # Update beta
                beta = min(beta, bestScore)
                if alpha >= beta:
                    break
    return bestScore, bestMove