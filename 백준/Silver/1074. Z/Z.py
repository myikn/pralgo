import sys

N, r, c = map(int, input().split())
result = 0

while N != 0:

    N -= 1
    
    # 1
    if r < 2 ** N and c < 2 ** N:
        continue
        
    # 2
    elif r < 2 ** N <= c:
        result += 2 ** (2 * N)
        c -= 2 ** N

    # 3
    elif r >= 2 ** N > c:
        result += 2 * 2 ** (2 * N)
        r -= 2 ** N

    # 4
    elif r >= 2 ** N and c >= 2 ** N:
        result += 3 * 2 ** (2 * N)
        r -= 2 ** N
        c -= 2 ** N

print(result)