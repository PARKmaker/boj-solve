import sys
si=sys.stdin.readline

M, N = map(int, si().split())
answer = []
def func(M, N):
    a = [0] * (N + 1)
    
    if M == 1:
        M = 2
    
    for i in range(2, N+1):
        a[i] = i
    for i in range(2, N+1):
        if a[i] == 0:
            continue
        for j in range(i+i, N+1, i):
            a[j] = 0

    for i in range(M, N+1):
        if a[i] != 0:
            print(a[i])

func(M, N)
