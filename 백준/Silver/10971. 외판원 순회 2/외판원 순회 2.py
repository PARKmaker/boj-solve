import sys
si = sys.stdin.readline

def dfs(start, next, value, k):
  global ans

  if k == n:
    if w[next][start]:
      value += w[next][start]
      if ans > value:
        ans = value
    return

  if value > ans:
    return

  for i in range(1, n+1):
    if used[i] or w[next][i] == 0:
      continue
    used[i] = 1
    dfs(start, i, value + w[next][i], k+1)
    used[i] = 0

n = int(si())
w = [[0 for _ in range(n)]]
used = [0 for _ in range(n+1)]
ans = 1 << 31

for _ in range(n):
  w.append([0] + list(map(int, si().split())))

for i in range(1, n+1):
  used[i] = 1
  dfs(i, i, 0, 1)
  used[i] = 0

print(ans)