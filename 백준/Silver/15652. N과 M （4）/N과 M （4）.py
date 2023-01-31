# https://www.acmicpc.net/problem/15652
import sys
si = sys.stdin.readline

N, M = map(int, si().split())

selected = [0 for _ in range(M)]
used = [0 for _ in range(0, N+1)]

def f(k):
  if k==M:
    for i in selected:
      print(i, end=" ")
    print()
  else:
    start = 1 if k==0 else selected[k-1]
    for cand in range(start, N+1):
      
      selected[k] = cand
      f(k+1)
      selected[k] = 0

f(0)