import sys

def dfs(y, x):
    global count
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[y][x] == 1:
        count += 1
        graph[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(ny, nx)
        return True
    return False


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
count = 0
result = 0
answer = []

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            answer.append(count)
            result += 1
            count = 0

answer.sort()
print(result)
for i in answer:
    print(i)