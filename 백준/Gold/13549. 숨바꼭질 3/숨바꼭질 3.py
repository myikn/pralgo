import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
queue = deque()
queue.append(m)
visited = [-1 for _ in range(100001)]
visited[m]=0

while queue:
    s = queue.popleft()
    if s == n:
        print(visited[s])
        break
        
    if 0 <= s-1 < 100001 and visited[s-1] == -1:
        visited[s-1] = visited[s] + 1
        queue.append(s-1)
        
    if 0 <= s*2 < 100001 and visited[s*2] == -1:
        visited[s*2] = visited[s]
        queue.appendleft(s*2)
        
    if 0 <= s+1 < 100001 and visited[s+1] == -1:
        visited[s+1] = visited[s] + 1
        queue.append(s+1)