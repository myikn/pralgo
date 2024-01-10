import sys

N = int(input())
M = int(input())

if M != 0:
    num_list = list(input().split())
else:
    num_list = []

result = abs(100 - N)

# 채널이 무한대이므로 올라가는것 내려가는것 모두 고려
for i in range(1000001):
    for j in str(i):
        if j in num_list:
            break
    else:
        result = min(result, len(str(i)) + abs(i - N))

print(result)