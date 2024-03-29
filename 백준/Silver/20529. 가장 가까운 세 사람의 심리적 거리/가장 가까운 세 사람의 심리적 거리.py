import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    if N > 32:
        sys.stdin.readline()
        print(0)

    else:
        mbti = list(sys.stdin.readline().split())
        result = 13
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    tmp = 0
                    for x in range(4):
                        if mbti[i][x] != mbti[j][x]: tmp += 1
                        if mbti[j][x] != mbti[k][x]: tmp += 1
                        if mbti[i][x] != mbti[k][x]: tmp += 1
                    result = min(tmp, result)
        print(result)
