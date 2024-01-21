import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    p = sys.stdin.readline().rstrip().replace('RR', '')
    n = int(sys.stdin.readline().rstrip())
    arr = deque()
    arr.extend(list(map(int, sys.stdin.readline().replace('[', '').replace(']', '').replace(',', ' ').split())))
    count = 0
    for i in p:
        if i == 'R':
            count += 1
        elif i == 'D':
            if not len(arr):
                print('error')
                break
            else:
                if count % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()

    else:
        if count % 2 == 1:
            arr.reverse()

        tmp = '['
        for j in arr:
            tmp += ',' + str(j)
        tmp += ']'

        res = list(tmp)
        if not len(res) == 2:
            del (res[1])
        res = "".join(res)

        print(res)