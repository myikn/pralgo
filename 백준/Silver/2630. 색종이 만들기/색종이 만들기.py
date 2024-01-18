import sys

def check(start_x, start_y, n):
    global white, blue
    color = graph[start_x][start_y]

    for i in range(start_x, start_x + n):
        for j in range(start_y, start_y + n):
            if color != graph[i][j]:
                check(start_x, start_y, n//2)
                check(start_x + n//2, start_y, n//2)
                check(start_x, start_y + n//2, n//2)
                check(start_x + n//2, start_y + n//2, n//2)
                return

    if color == 1:
        white += 1
    elif color == 0:
        blue += 1

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0

check(0, 0, N)
print(blue)
print(white)