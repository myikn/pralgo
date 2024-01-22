import sys

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    tmp = x

    if M == 1 or N == 1:
        if M == 1:
            print(-1 if x > 1 else y)

        elif N == 1:
            print(-1 if y > 1 else x)

    else:
        flag = 0
        while tmp <= M * N:
            if (tmp - x) % M == 0 and (tmp - y) % N == 0:
                flag = 1
                break
            tmp += M
        print(tmp if flag else -1)