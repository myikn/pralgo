import sys
N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().split()))

tmp = {x: i for i, x in enumerate(sorted(set(X)))}
result = [tmp[x] for x in X]
print(*result)
