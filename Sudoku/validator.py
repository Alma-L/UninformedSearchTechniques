def is_in_subgrid(grid, row, col, num):
    #Kontrollo nese nje numer ekziston brenda nen-bllokut 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return True
    return False

def is_valid_move(grid, row, col, num):
    #Kontrollo nese nje numer mund te vendoset ne rreshtin, kolonen dhe nen-tabelen.
    # Kontrollo rreshtin
    if num in grid[row]:
        return False

    # Kontrollo kolonen
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Kontrollo nen-bllokun 3x3
    if is_in_subgrid(grid, row, col, num):
        return False

    return True
