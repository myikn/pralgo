import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split(' '))
tmp = [i for i in range(1, N + 1)]
a = permutations(tmp, M)

for perm in a:
    print(' '.join(map(str, perm)))