import random
import numpy as np


def generate_valid_latin_square(n, empty_fraction=0.2):
    """
    Generates a valid n x n Latin square with some empty cells.

    :param n: Size of the board (n x n).
    :param empty_fraction: Fraction of the board to be empty (default 20%).
    :return: A valid Latin square with some empty cells.
    """
    # Step 1: Generate a valid Latin square
    square = np.zeros((n, n), dtype=int)
    for i in range(n):
        square[i] = np.roll(np.arange(1, n + 1), -i)

    # Randomize rows and columns for variety
    np.random.shuffle(square)
    square = square[:, np.random.permutation(n)]

    # Step 2: Remove cells to create a puzzle
    num_cells = n * n
    num_to_remove = int(num_cells * empty_fraction)
    cells_to_remove = random.sample(range(num_cells), num_to_remove)

    for cell in cells_to_remove:
        row = cell // n
        col = cell % n
        square[row, col] = 0

    return square.tolist()


def iddfs_solve(board):
    """
    Solves the puzzle using IDDFS and backtracking.
    """
    depth_limit = 1
    max_depth = len(board) ** 2

    while depth_limit <= max_depth:
        if depth_limited_solve(board, depth_limit):
            return True
        depth_limit += 1

    return False


def depth_limited_solve(board, depth_limit):
    """
    Performs a depth-limited search with backtracking.
    """
    if depth_limit == 0:
        return False

    find = find_empty(board)
    if not find:
        return True  # Solution found
    else:
        row, col = find

    for i in range(1, len(board) + 1):
        if valid(board, i, (row, col)):
            board[row][col] = i

            # Recursive call with decreased depth limit
            if depth_limited_solve(board, depth_limit - 1):
                return True

            # Undo the move (backtracking)
            board[row][col] = 0

    return False


def valid(board, num, pos):
    """
    Checks if placing a number in a specific position is valid for a Latin square.
    """
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num:
            return False

    return True


def print_board(board):
    """
    Prints the board in a readable format.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == (len(board) - 1):
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print()


def find_empty(board):
    """
    Finds the next empty cell in the board.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col

    return None


if __name__ == "__main__":
    n = int(input("Enter the size of the board (n x n): "))
    empty_fraction = float(input("Enter the fraction of empty cells (e.g., 0.5 for 50% empty): "))

    # Generate the random board
    matrix = generate_valid_latin_square(n, empty_fraction)

    print("Generated Board:")
    print_board(matrix)

    if iddfs_solve(matrix):
        print("Solved Board:")
        print_board(matrix)
    else:
        print("No solution exists.")
