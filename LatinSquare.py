def is_safe(matrix, row, col, num, n):
    """Check if placing `num` at position (row, col) is valid."""
    return all(matrix[row][x] != num for x in range(n)) and all(matrix[x][col] != num for x in range(n))


def solve_with_backtracking(matrix, depth, n):
    """
    Solve the Latin square using backtracking up to the given depth.
    """
    if depth == n * n:
        return True  # All cells are filled, solution found.

    row, col = divmod(depth, n)  # Get the current cell (row, col).

    if matrix[row][col] != 0:  # If already filled, go to the next cell.
        return solve_with_backtracking(matrix, depth + 1, n)

    for num in range(1, n + 1):  # Try all possible numbers from 1 to n.
        if is_safe(matrix, row, col, num, n):
            matrix[row][col] = num  # Place the number.
            if solve_with_backtracking(matrix, depth + 1, n):  # Recur for the next cell.
                return True
            matrix[row][col] = 0  # Undo the placement (backtrack).

    return False  # No valid number found, backtrack.


def generate_latin_square(n):
    """
    Generate a Latin square of size n x n using backtracking.
    """
    matrix = [[0] * n for _ in range(n)]  # Initialize an n x n matrix with zeros.
    if solve_with_backtracking(matrix, 0, n):  # Solve using backtracking.
        return matrix
    return None  # Return None if no solution exists.


def print_latin_square(matrix):
    """
    Print the Latin square in a readable format.
    """
    for row in matrix:
        print(' '.join(map(str, row)))


def latin_square_generator():

    try:
        n = int(input("Please write the number you want Latin Square to be generated: "))
        if n <= 0:
            print("The number must be a positive integer greater than 0!")
            return

        latin_square = generate_latin_square(n)  # Generate the Latin square.
        if latin_square:
            print("Generated Latin Square:")
            print_latin_square(latin_square)
        else:
            print("No solution found!")
    except ValueError:
        print("Invalid input! Please enter a valid positive integer.")


#main function
if __name__ == "__main__":
    latin_square_generator()
