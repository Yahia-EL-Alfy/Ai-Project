import numpy as np
import random
from colorama import init, Fore, Style
from tkinter import *
import boardd
import Minimax
import Alpha_beta
import GUI
import game
import time

#boardd -> is a class while board is a variable


# Define the main function to play the game between an AI agent and a computer
def main():
    # GUI.guui()
    # Initialize the board
    board = np.zeros((6, 7), dtype=int)
    # Start the game
    currentPlayer = 1
    # ask user for algorithm type
    chooseAlgorithm = None
    c = GUI.choose(chooseAlgorithm)

    # print(f"c={c}")
    # print(f"difff {set_difficulty_level()}")

    if str(c) == "1":
        minimax_func = Minimax.minimax
        algorithm_name = "Minimax"
    else:
        minimax_func = Alpha_beta.minimax_alpha_beta
        algorithm_name = "Minimax with Alpha-Beta pruning"

    print("Playing with", algorithm_name)

    difficulty_level = GUI.set_difficulty_level()
    print(f"Your difficulty level is { difficulty_level}")
    max_depth = 2 + difficulty_level



    if str(c) == "1":
        while True:
            # Print the board
            print("\n")
            for row in board:
                for cell in row:
                    if cell == 0:
                        print(boardd.EMPTY_CELL_COLOR + "⚪" + Style.RESET_ALL, end=" ")
                    else:
                        print(boardd.PLAYER_COLORS[cell] + "⚫" + Style.RESET_ALL, end=" ")
                print()
            print(Fore.YELLOW + "-" * 21 + Style.RESET_ALL)
            # Get the player's move or AI agent's move

            if currentPlayer == 1:
                start_time = time.time()  # Record start time
                _, col = Minimax.minimax(board, max_depth, True)
                end_time = time.time()  # Record end time
                time_taken = end_time - start_time  # Calculate time taken
                # Make move
                row = 5
                while row >= 0 and board[row][col] != 0:
                    row -= 1
                board[row][col] = 1
                print(boardd.PLAYER_COLORS[1] + "AI agent" + Style.RESET_ALL + " chose column", col + 1, "in", time_taken.__round__(3), "seconds")
            else:
                start_time = time.time()  # Record start time
                valid_moves = [col for col in range(7) if board[0][col] == 0]
                col = random.choice(valid_moves)
                end_time = time.time()  # Record end time
                time_taken = end_time - start_time  # Calculate time taken
                # Make move
                row = 5
                while row >= 0 and board[row][col] != 0:
                    row -= 1
                board[row][col] = 2

                print(boardd.PLAYER_COLORS[2] + "Computer" + Style.RESET_ALL + " chose column", col + 1, "in", time_taken.__round__(3), "seconds")
            # Check for win or draw
            score = game.evaluate(board)
            if score == 100:
                print("\n")
                for row in board:
                    for cell in row:
                        if cell == 0:
                            print(boardd.EMPTY_CELL_COLOR + "⚪" + Style.RESET_ALL, end=" ")
                        else:
                            print(boardd.PLAYER_COLORS[cell] + "⚫" + Style.RESET_ALL, end=" ")
                    print()
                print(Fore.YELLOW + "-" * 21 + Style.RESET_ALL)
                print("\n" + boardd.PLAYER_COLORS[1] + "AI agent" + Style.RESET_ALL + " wins!")
                break
            elif score == -100:
                print("\n")
                for row in board:
                    for cell in row:
                        if cell == 0:
                            print(boardd.EMPTY_CELL_COLOR + "⚪" + Style.RESET_ALL, end=" ")
                        else:
                            print(boardd.PLAYER_COLORS[cell] + "⚫" + Style.RESET_ALL, end=" ")
                    print()
                print(Fore.YELLOW + "-" * 21 + Style.RESET_ALL)
                print("\n" + boardd.PLAYER_COLORS[2] + "Computer" + Style.RESET_ALL + " wins!")
                break
            elif np.count_nonzero(board) == 42:
                print("\nDraw!")
                break
            # Switch players
            currentPlayer = 3 - currentPlayer
    else:
        while True:
            boardd.print_board(board)
            if currentPlayer == 1:
                start_time = time.time()  # Record start time
                _, col = Alpha_beta.minimax_alpha_beta(board, max_depth, -np.inf, np.inf, True)
                end_time = time.time()  # Record end time
                time_taken = end_time - start_time  # Calculate time taken
                # Make move
                row = 5
                while row >= 0 and board[row][col] != 0:
                    row -= 1
                board[row][col] = 1
                print(boardd.PLAYER_COLORS[1] + "AI agent" + Style.RESET_ALL + " chose column", col + 1, "in", time_taken.__round__(3), "seconds")
            else:
                start_time = time.time()  # Record start time
                valid_moves = [col for col in range(7) if board[0][col] == 0]
                col = random.choice(valid_moves)
                end_time = time.time()  # Record end time
                time_taken = end_time - start_time  # Calculate time taken
                # Make move
                row = 5
                while row >= 0 and board[row][col] != 0:
                    row -= 1
                board[row][col] = 2

                print(boardd.PLAYER_COLORS[2] + "Computer" + Style.RESET_ALL + " chose column", col + 1, "in", time_taken.__round__(3), "seconds")
            # Check for win or draw
            score = game.evaluate(board)
            if score == 100:
                print("\n")
                for row in board:
                    for cell in row:
                        if cell == 0:
                            print(boardd.EMPTY_CELL_COLOR + "⚪" + Style.RESET_ALL, end=" ")
                        else:
                            print(boardd.PLAYER_COLORS[cell] + "⚫" + Style.RESET_ALL, end=" ")
                    print()
                print(Fore.YELLOW + "-" * 21 + Style.RESET_ALL)
                print("\n" + boardd.PLAYER_COLORS[1] + "AI agent" + Style.RESET_ALL + " wins!")
                break
            elif score == -100:
                print("\n")
                for row in board:
                    for cell in row:
                        if cell == 0:
                            print(boardd.EMPTY_CELL_COLOR + "⚪" + Style.RESET_ALL, end=" ")
                        else:
                            print(boardd.PLAYER_COLORS[cell] + "⚫" + Style.RESET_ALL, end=" ")
                    print()
                print(Fore.YELLOW + "-" * 21 + Style.RESET_ALL)
                print("\n" + boardd.PLAYER_COLORS[2] + "Computer" + Style.RESET_ALL + " wins!")
                break
            elif np.count_nonzero(board) == 42:
                print("\nDraw!")
                break
            # Switch players
            currentPlayer = 3 - currentPlayer

main()