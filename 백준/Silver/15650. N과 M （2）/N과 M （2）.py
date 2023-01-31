import sys
si = sys.stdin.readline

n, m = map(int, si().split())

used = [0 for _ in range(n+1)]
selected = [0 for _ in range(m)]

def rec_func(k):
  
  if k == m:
    print(*selected)
    return

  cand = 1 if k == 0 else selected[k-1] + 1

  for i in range(cand, n+1):
    if used[i]:
      continue
    selected[k] = i
    used[i] = 1
    rec_func(k+1)
    selected[k] = 0
    used[i] = 0

rec_func(0)