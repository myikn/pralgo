from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    result = 0
    queue = deque([(a, b)])
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if campus[nx][ny] != 'X' and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

                    if campus[nx][ny] == 'P':
                        result += 1
    return result


N, M = map(int, input().split())
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * M for _ in range(N)]
campus = []
start_x = 0
start_y = 0

for i in range(N):
    a = list(input().rstrip())
    for j in range(M):
        if a[j] == 'I':
            start_x = i
            start_y = j
    campus.append(a)

tmp = bfs(start_x, start_y)
print(tmp if tmp > 0 else 'TT')