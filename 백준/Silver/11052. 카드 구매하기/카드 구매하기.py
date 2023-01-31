import sys
si=sys.stdin.readline

N = int(si())

P = [0] + list(map(int, si().split()))

a = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for k in range(1, i+1):
        a[i] = max(a[i], a[i-k] + P[k])

print(a[N])
