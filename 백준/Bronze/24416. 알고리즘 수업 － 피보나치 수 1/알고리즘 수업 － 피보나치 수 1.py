# https://www.acmicpc.net/problem/24416

import sys
si = sys.stdin.readline

N = int(si())

f = [0 for _ in range(N)]

def fib(n):
  f[0] = f[1] = 1
  for i in range(2, n):
    f[i] = f[i-1] + f[i-2]
  
  return f[n-1]

print(fib(N), N-2)