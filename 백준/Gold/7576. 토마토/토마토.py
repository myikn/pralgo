import sys
from collections import deque

def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result = 0
bfs()

flag = 0
for i in range(N):
    for j in range(M):
        result = max(result, graph[i][j])
        if graph[i][j] == 0:
            print(-1)
            flag = 1
            break
    if flag:
        break
else:
    print(result - 1)