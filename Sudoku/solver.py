from collections import deque
from validator import is_valid_move
import random

def solve_sudoku_backtracking(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # Sudoku eshte zgjidhur

    row, col = empty_cell
    random_numbers = list(range(1, 10))
    random.shuffle(random_numbers)


    for num in random_numbers:
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num  # Vendos numrin

            if solve_sudoku_backtracking(grid):  # Teston tabelen ne vazhdim
                return True

            grid[row][col] = 0  # Kthehu mbrapsht (backtrack)

    return False  # Nuk ka zgjidhje

def find_empty_cell(grid):
    #Gjej vleren e pare me vlerë 0
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None  # Nuk ka velra 0

def bfs_solver(grid):
    queue = deque([grid])  # Queue per gjendjet e tabeles

    while queue:
        current_grid = queue.popleft()

        # Gjej qelizen me vlere 0
        found_empty = False
        for row in range(9):
            for col in range(9):
                if current_grid[row][col] == 0:
                    # Gjej qelizen me vlere 0 dhe provo numrat 1-9
                    found_empty = True
                    for num in range(1, 10):
                        if is_valid_move(current_grid, row, col, num):
                            # Gjenero nje gjendje te re dhe shtoje në radhe
                            new_grid = [list(r) for r in current_grid]  # Kopjo tabelen
                            new_grid[row][col] = num
                            queue.append(new_grid)
                    break
            if found_empty:
                break

        # Nese nuk ka me vlera 0, kthe zgjidhjen
        if not found_empty:
            return current_grid

    # Nese nuk ka zgjidhje
    return None
