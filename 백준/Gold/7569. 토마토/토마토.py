import sys
from collections import deque

def bfs():
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))

    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + direction[i][0]
            nx = x + direction[i][1]
            ny = y + direction[i][2]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz, nx, ny))


M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# z x y
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
result = 0
bfs()

flag = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            result = max(result, graph[i][j][k])
            if graph[i][j][k] == 0:
                print(-1)
                flag = 1
                break

        if flag:
            break
    if flag:
        break

else:
    print(result - 1)