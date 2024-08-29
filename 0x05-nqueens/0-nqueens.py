#!/usr/bin/python3
"""
N Queens solution
"""
import sys


def is_valid(board, row, col):
    # Checking the row on left side
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Checking the upper diagonal on left side
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    # Checking the lower diagonal on left side
    for r, c in zip(range(row, len(board)), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    return True


def place_queens(board, col):
    if col >= len(board):
        display_solution(board)
        return True

    solution_found = False
    for row in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 1
            solution_found = place_queens(board, col + 1) or solution_found
            board[row][col] = 0  # Undo the move (backtrack)

    return solution_found


def display_solution(board):
    result = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                result.append([row, col])
    print(result)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0 for _ in range(N)] for _ in range(N)]
place_queens(board, 0)
