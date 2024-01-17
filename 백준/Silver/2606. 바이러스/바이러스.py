import sys

def bfs(n):
    queue = [n]
    visited[n] = 1

    while queue:
        x = queue.pop(0)
        visited[x] = 1
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = list([] for _ in range(N + 1))
visited = list(0 for _ in range(N + 1))

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

print(visited.count(1) - 1)