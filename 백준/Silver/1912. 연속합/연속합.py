import sys
si = sys.stdin.readline

N = int(si())

a = list(map(int, si().split()))

for i in range(1, N):
  a[i] = max(a[i] , a[i-1] + a[i])

print(max(a))