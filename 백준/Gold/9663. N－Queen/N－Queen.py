import sys


def is_safe(queens, row, col):
    for r, c in enumerate(queens):
        if col == c or abs(col - c) == abs(row - r):
            return False
    return True


def backtrack(row, queens, n):
    if row == n:
        result.append(queens[:])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            backtrack(row + 1, queens, n)
            queens.pop()


N = int(sys.stdin.readline().rstrip())
result = []
backtrack(0, [], N)
print(len(result))