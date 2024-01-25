import sys

T = int(input())
for _ in range(T):
    n = int(input())
    tmp = {}
    result = 1
    for _ in range(n):
        a, b = sys.stdin.readline().split()

        if not b in tmp:
            tmp[b] = 1
        else:
            tmp[b] += 1

    for value in tmp.values():
        result *= (value + 1)

    print(result - 1)