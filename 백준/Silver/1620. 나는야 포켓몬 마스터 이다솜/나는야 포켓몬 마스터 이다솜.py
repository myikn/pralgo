import sys

N, M = map(int, sys.stdin.readline().split())
dogam = {}

for i in range(1, N + 1):
    name = sys.stdin.readline().strip()
    dogam[name] = str(i)
    dogam[str(i)] = name

for _ in range(M):
    print(dogam[str(sys.stdin.readline().strip())])