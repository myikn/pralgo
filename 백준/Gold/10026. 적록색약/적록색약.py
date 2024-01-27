import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < N and 0 <= ny < N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                queue.append((nx, ny))


N = int(sys.stdin.readline().rstrip())
a = [list(sys.stdin.readline()) for _ in range(N)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1
            
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)