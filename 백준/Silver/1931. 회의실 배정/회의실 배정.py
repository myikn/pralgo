import sys

N = int(sys.stdin.readline().rstrip())
tmp = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    tmp.append((a, b))

tmp.sort(key=lambda x: (x[1], x[0]))
start = 0
cnt = 0

for i in tmp:
    if i[0] < start:
        continue
    cnt += 1
    start = i[1]

print(cnt)