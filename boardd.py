import numpy as np
import random
from colorama import init, Fore, Style
from tkinter import *


# Initialize colorama for colored output
init()

# Define colors for the players
PLAYERS = {1: "AI Agent", 2: "Computer"}
PLAYER_COLORS = {1: Fore.BLUE, 2: Fore.RED}
EMPTY_CELL_COLOR = Fore.WHITE


def print_board(board):
    # Print the board
    print("\n")
    for row in board:
        for cell in row:
            if cell == 0:
                print(EMPTY_CELL_COLOR + "⚪" + Style.RESET_ALL, end=" ")
            else:
                print(PLAYER_COLORS[cell] + "⚫" + Style.RESET_ALL, end=" ")
        print()
    print(Fore.YELLOW + "-" * 21 + Style.RESET_ALL)
