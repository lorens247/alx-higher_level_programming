#!/usr/bin/python3
# 101-rectangle.py by Lawrence Ikhidero
"""
The n queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. This program solves the n queens problem by printing every
possible solution to the problem, with one solution per line.
"""

import sys

def is_safe(board, row, col):
    """
    A utility function to check if a queen can be placed on board[row][col].
    This function is called when a new queen is being placed in column 'col',
    at row 'row'. It returns True if the placement is safe, otherwise False.
    """

    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # The placement is safe
    return True

def solve_nqueens(board, col, solutions):
    """
    A recursive utility function to solve the n queens problem. It returns
    True if the problem has been solved, otherwise False. The function takes
    the current board, the current column being considered, and a list of
    all the solutions found so far. If a solution is found, it is appended
    to the solutions list.
    """

    # Base case: all queens have been placed
    if col >= len(board):
        solution = [[row, board[row].index(1)] for row in range(len(board))]
        solutions.append(solution)
        return True

    # Try placing the queen in each row of the current column
    for row in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen in this position
            board[row][col] = 1

            # Check if this placement leads to a solution
            if solve_nqueens(board, col+1, solutions):
                return True

            # If not, backtrack and remove the queen from this position
            board[row][col] = 0

    # No solution found
    return False

def nqueens(n):
    """
    Solve the n queens problem for a board of size n.
    """

    # Check that n is a valid input
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    elif n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board to all zeros
    board = [[0 for x in range(n)] for y in range(n)]

    # Solve the problem and print the solutions
    solutions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)

if __name__ == '__main__':
    # Check that the program was called with the correct arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the size of the board from the command line argument
   
