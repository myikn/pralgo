import sys

N, M = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

tmp_list = [0]
sum_number = 0
for i in number:
    sum_number += i
    tmp_list.append(sum_number)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(tmp_list[j] - tmp_list[i-1])