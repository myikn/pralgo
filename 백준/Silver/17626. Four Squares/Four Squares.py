import sys

def foursquare(N):
    # 1
    if int(N ** 0.5) == N ** 0.5:
        return 1

    # 2
    for i in range(1, int(N ** 0.5) + 1):
        if int((N - i**2) ** 0.5) == (N - i**2) ** 0.5:
            return 2

    # 3
    for i in range(1, int(N ** 0.5) + 1):
        for j in range(1, int((N - i**2) ** 0.5) + 1):
            if int((N - i**2 - j**2) ** 0.5) == (N - i**2 - j**2) ** 0.5:
                return 3

    # 4
    return 4

N = int(sys.stdin.readline().rstrip())
print(foursquare(N))