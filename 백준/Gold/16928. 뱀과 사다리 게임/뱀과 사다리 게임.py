import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        x = queue.popleft()
        if x == 100:
            print(result[100])
            break

        for i in range(1, 7):
            nx = x + i
            if nx <= 100 and not visited[nx]:
                if nx in move.keys():
                    nx = move[nx]

                if not visited[nx]:
                    visited[nx] = 1
                    result[nx] = result[x] + 1
                    queue.append(nx)

N, M = map(int, sys.stdin.readline().split())
move = {}
for _ in range(N+M):
    a, b = map(int, sys.stdin.readline().split())
    move[a] = b

result = [0] * 101
visited = [0] * 101
bfs()
