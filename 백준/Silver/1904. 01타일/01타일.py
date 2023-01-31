#https://www.acmicpc.net/problem/1904

import sys
si = sys.stdin.readline

N = int(si())

f = [0 for _ in range(N+2)]

def dy(x):
  f[1], f[2] = 1 , 2

  if x >= 3:
    for i in range(3, x+1):
      f[i] = f[i-1] + f[i-2]
      if i > 15746:
        f[i] = f[i] % 15746

  return f[x]

print(dy(N) % 15746)