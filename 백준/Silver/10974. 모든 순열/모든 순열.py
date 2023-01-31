import sys
si = sys.stdin.readline

n = int(si())

used = [0 for _ in range(n+1)]
selected = [0 for _ in range(n)]

def dfs(k):
  
  if k == n:
    print(*selected)
    return

  for cand in range(1, n+1):
    if used[cand]:
      continue

    selected[k] = cand
    used[cand] = 1
    dfs(k+1)
    selected[k] = 0
    used[cand] = 0

dfs(0)