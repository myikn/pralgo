import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start = 1
end = max(tree)

while start <= end:
    middle = (start + end) // 2
    result = 0

    for i in tree:
        if i >= middle:
            result += (i - middle)

    if result >= M:
        start = middle + 1
    else:
        end = middle - 1

print(end)