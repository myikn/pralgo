import sys


def is_safe(row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for y in range(9):
        if board[y][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def solve_sudoku():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(row, col, num):
                        board[row][col] = num
                        if solve_sudoku():
                            return True
                        board[row][col] = 0
                return False
    return True


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
solve_sudoku()

for result in board:
    print(' '.join(map(str, result)))