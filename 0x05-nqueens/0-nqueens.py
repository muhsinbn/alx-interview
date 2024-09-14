#!/usr/bin/python3
""" Module that solves the nqueens challenge."""
import sys


def is_valid(board, row, col):
    """
    Check if a queen can be placed at board[row][col].

    Args:
        board (list): Current state of the board.
        row (int): Row index.
        col (int): Column index.

    Returns:
        bool: True if no other queens threaten the position,
        False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def place_queens(board, row, n, solutions):
    """
    Recursively place queens on the board.

    Args:
        board (list): Current state of the board.
        row (int): Current row to place the queen.
        n (int): Size of the board.
        solutions (list): List to store all valid solutions.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            place_queens(board, row + 1, n, solutions)
            board[row] = -1


def solve_n_queens(n):
    """
    Solve the N-Queens problem.

    Args:
        n (int): Size of the board.

    Returns:
        list: List of all valid solutions, where each solution is a
        list representing queen positions.
    """
    solutions = []
    board = [-1] * n
    place_queens(board, 0, n, solutions)
    return solutions


def print_solutions(solutions, n):
    """
    Print all solutions in the required format.

    Args:
        solutions (list): List of all valid solutions.
        n (int): Size of the board.
    """
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(n)]
        print(formatted_solution)


def main():
    """
    Main function to handle command-line arguments and solve
    the N-Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    print_solutions(solutions, n)


if __name__ == "__main__":
    main()
