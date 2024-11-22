def is_safe(matrix, row, col, num, n):
    # Check if 'num' can be placed at matrix[row][col]
    for x in range(n):
        if matrix[row][x] == num or matrix[x][col] == num:
            return False
    return True


def backtrack_with_depth(matrix, depth, max_depth, n):
    # If depth exceeds max_depth, terminate this branch
    if depth > max_depth:
        return False

    # If all cells are filled, we have a solution
    if depth == n * n:
        return True

    row, col = divmod(depth, n)  # Get current cell (row, col)

    # If the cell is already filled, move to the next depth
    if matrix[row][col] != 0:
        return backtrack_with_depth(matrix, depth + 1, max_depth, n)

    # Try placing numbers from 1 to n
    for num in range(1, n + 1):
        if is_safe(matrix, row, col, num, n):
            matrix[row][col] = num
            # Recur for the next cell
            if backtrack_with_depth(matrix, depth + 1, max_depth, n):
                return True
            # Undo placement
            matrix[row][col] = 0

    return False


def iddfs_with_backtracking(matrix, n):
    # Iteratively increase the depth limit
    for max_depth in range(1, n * n + 1):
        if backtrack_with_depth(matrix, 0, max_depth, n):
            return True
    return False


def latin_square_iddfs_backtracking():
    try:
        # Prompt user for input
        n = int(input("Please write the number you want the Latin Square to be generated: "))
        if n <= 0:
            print("The number must be greater than 0!")
            return

        # Initialize the matrix
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        # Solve using IDDFS with Backtracking
        if iddfs_with_backtracking(matrix, n):
            print("Latin Square:")
            for row in matrix:
                print(' '.join(map(str, row)))
        else:
            print("No solution found!")
    except ValueError:
        print("Invalid input! Please enter a positive integer.")


# Run the function
latin_square_iddfs_backtracking()
