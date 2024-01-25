import sys

T = int(input())
for _ in range(T):
    P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    N = int(input())
    
    while len(P) <= N:
        P.append(P[-3] + P[-2])
        
    print(P[N-1])