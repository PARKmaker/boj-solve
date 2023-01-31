#https://www.acmicpc.net/problem/2579

import sys
si = sys.stdin.readline

N = int(si())

arr = [0] * N

for i in range(N):
  arr[i] = int(si())

a = [[0,0] for _ in range(N+2)]

a[0][0], a[0][1] = 0, arr[0]

if N >= 2:
    a[1][0], a[1][1] = arr[1], arr[0] + arr[1]

for i in range(2, N):
  
  a[i][0] = max(a[i-2][0], a[i-2][1]) + arr[i]
  a[i][1] = a[i-1][0] + arr[i]


print(max(a[N-1][0],a[N-1][1]))