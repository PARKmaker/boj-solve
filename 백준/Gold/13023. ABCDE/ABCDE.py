import sys
si = sys.stdin.readline
n, m = map(int, si().split())
adj = [[] for _ in range(n)]

for i in range(m):
  x, y = map(int, si().split())
  adj[x].append(y)
  adj[y].append(x)

for i in range(n):
  adj[i].sort()

visited = [False for i in range(n)]
ans = 0
def dfs(i, depth):
  global ans
  visited[i] = True

  if depth == 4:
    ans = 1
    return
  
  for x in adj[i]:
    if visited[x]:
      continue
    
    dfs(x, depth+1)
    visited[x] = False

for i in range(n):
  dfs(i,0)
  visited[i] = False

  if ans:
    break

print(ans)