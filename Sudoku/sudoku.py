from generate import generate_sudoku
from solver import bfs_solver, solve_sudoku_backtracking
from print import print_sudoku

def main():
    difficulty = "hard"
    sudoku_puzzle = generate_sudoku(difficulty)

    print("Tabela e gjeneruar:")
    print_sudoku(sudoku_puzzle)

    solved_backtracking = [row[:] for row in sudoku_puzzle] #kopjon matricen
    if solve_sudoku_backtracking(solved_backtracking):
        print("\n\nZgjidhja me Backtracking:")
        print_sudoku(solved_backtracking)
    else:
        print("Nuk ka zgjidhje me Backtracking.")

    solved_bfs = bfs_solver(sudoku_puzzle)
    if solved_bfs:
        print("\n\nZgjidhja me BFS:")
        print_sudoku(solved_bfs)
    else:
        print("Nuk ka zgjidhje me BFS.")

if __name__ == "__main__":
    main()
