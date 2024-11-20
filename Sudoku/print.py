def print_sudoku(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("-- " * 9)

        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")
            print(str(num) if num != 0 else "_", end=" ")
        print()
