import sys
N = int(sys.stdin.readline().rstrip())
result = [1, 3, 5]

while len(result) < N:
    result.append(2 * result[-2] + result[-1])

print(result[N-1] % 10007)