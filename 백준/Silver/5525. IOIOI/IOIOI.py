import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().split('I')

cnt = 0
result = 0
for i in S:
    if i == 'O':
        cnt += 1
    else:
        cnt = 0

    if cnt == N:
        result += 1
        cnt -= 1

print(result)