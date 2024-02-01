import sys

M = int(sys.stdin.readline().rstrip())
S = set()

for _ in range(M):
    tmp = sys.stdin.readline().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif tmp[0] == 'empty':
            S = set()

    else:
        command, number = tmp[0], int(tmp[1])

        if command == 'add':
            S.add(number)

        elif command == 'remove':
            S.discard(number)

        elif command == 'check':
            print(1 if number in S else 0)

        elif command == 'toggle':
            S.discard(number) if number in S else S.add(number)