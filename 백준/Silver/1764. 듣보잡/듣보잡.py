import sys

N, M = map(int, sys.stdin.readline().split())
tmp = set()
cnt = 0
result = []

for _ in range(N):
    tmp.add(sys.stdin.readline().strip())

for _ in range(M):
    comp = sys.stdin.readline().strip()
    if comp in tmp:
       cnt += 1
       result.append(comp)

result.sort()
print(cnt)
for i in result:
    print(i.replace("\n", ""))