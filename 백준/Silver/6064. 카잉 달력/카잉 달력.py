import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    if M == 1 or N == 1:
        if M == 1:
            print(-1 if x > 1 else y)

        elif N == 1:
            print(-1 if y > 1 else x)

    else:
        max_year = lcm(M, N)
        for i in range(max_year // M):
            year = i * M + x
            ny = N if year % N == 0 else year % N
            if ny == y:
                print(year)
                break
        else:
            print(-1)