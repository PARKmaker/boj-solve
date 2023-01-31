# https://www.acmicpc.net/problem/9663
import sys
si = sys.stdin.readline

N = int(si())
col = [0 for _ in range(N)]
ans = 0

def attackable(r1, c1, r2, c2):
  if c1 == c2:
    return True
  if r1 - c1 == r2 - c2:
    return True
  if r1 + c1 == r2 + c2:
    return True
  return False

def f(row):
  if row == N:
    global ans
    ans += 1
  
  else:
    for cand in range(N):
      possible = True
      for i in range(row):
        if attackable(row, cand, i, col[i]):
          possible = False
          break
      
      if possible:
        col[row] = cand
        f(row+1)
        col[row] = 0

f(0)
print(ans)