import sys

N = int(sys.stdin.readline().rstrip())
stairs = [0]

for i in range(1, N + 1):
    stairs.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (N + 1)
dp[1] = stairs[1]
if N >= 2:
    dp[2] = dp[1] + stairs[2]

if N >= 3:
    # 0 1 3이 큰 지, 0 2 3이 큰 지 비교, 0 1 2 3은 불가능
    dp[3] = max(dp[1] + stairs[3], stairs[2] + stairs[3])

    # 1 3 4 인지 2 4인지
    for j in range(4, N + 1):
        dp[j] = max(dp[j-3] + stairs[j-1] + stairs[j], dp[j-2] + stairs[j])

print(dp[N])