import sys
from collections import deque


def bfs(n):
    queue = deque()
    queue.append(n)
    graph[n] = 0

    while queue:
        a = queue.popleft()

        if a == K:
            break

        if 0 <= a + 1 <= 100000:
            if graph[a + 1] == 0 or graph[a] + 1 <= graph[a + 1]:
                graph[a + 1] = graph[a] + 1
                queue.append(a + 1)

        if 0 <= a - 1 <= 100000:
            if graph[a - 1] == 0 or graph[a] + 1 <= graph[a - 1]:
                graph[a - 1] = graph[a] + 1
                queue.append(a - 1)

        if 0 <= a * 2 <= 100000:
            if graph[a * 2] == 0 or graph[a] + 1 <= graph[a * 2]:
                graph[a * 2] = graph[a] + 1
                queue.append(a * 2)


N, K = map(int, sys.stdin.readline().split())
graph = [0 for _ in range(100001)]
bfs(N)
print(graph[K])