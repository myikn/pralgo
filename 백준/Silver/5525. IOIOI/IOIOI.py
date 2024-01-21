import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = deque()
S.extend(sys.stdin.readline().split('I'))

cnt = 0
result = 0

if S[0] != '':
    S.popleft()

for i in S:
    if i == 'O':
        cnt += 1
    else:
        cnt = 0

    if cnt == N:
        result += 1
        cnt -= 1

if M < 3:
    print(0)

else:
    print(result)