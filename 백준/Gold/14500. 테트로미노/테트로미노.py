import sys

def tetromino(x, y):
    global answer
    for k in range(19):
        tmp = 0
        for l in range(4):
            nx = x + array[k][l][0]
            ny = y + array[k][l][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break

            tmp += graph[nx][ny]
        answer = max(answer, tmp)

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
array = [
    # ㅡ ㅣ ㅁ L L회전3 L대칭 L대칭회전3 h h회전 h대칭 h대칭회전 ㅜ ㅓ ㅗ ㅏ = 19가지경우
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(0, 1), (1, 1), (2, 1), (1, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)]
]

answer = 0
for i in range(N):
    for j in range(M):
        tetromino(i, j)

print(answer)