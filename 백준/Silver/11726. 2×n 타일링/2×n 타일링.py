import sys

N = int(sys.stdin.readline().rstrip())
result = [1, 2, 3]

while len(result) < N:
    result.append(result[-2] + result[-1])

print(result[N-1] % 10007)