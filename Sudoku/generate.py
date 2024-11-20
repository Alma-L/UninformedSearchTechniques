import random
from solver import solve_sudoku_backtracking

def generate_full_sudoku():
    """Krijo nje tabele Sudoku te plote duke perdorur Backtracking."""
    grid = [[0] * 9 for _ in range(9)]  # Tabela me vlera 0
    solve_sudoku_backtracking(grid)  # Gjeneron nje tabele te mbushur
    return grid

def remove_cells(grid, difficulty):
    """Hiq qelizat nga nje tabele Sudoku per te percaktuar nivelin e veshtiresise."""
    cells_to_remove = {
        "easy": 30,
        "medium": 40,
        "hard": 50
    }.get(difficulty, 30)  # Default: easy

    while cells_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:  # Sigurohemi qe te mos heqim dy here te njejten qelize
            grid[row][col] = 0
            cells_to_remove -= 1

    return grid

def generate_sudoku(difficulty="easy"):
    """Gjenero nje tabele Sudoku per nje nivel te dhene veshtiresie."""
    full_grid = generate_full_sudoku()  # Gjenero nje tabele te plote
    puzzle = remove_cells(full_grid, difficulty)  # Hiq vlera per te krijuar hapsira
    return puzzle
