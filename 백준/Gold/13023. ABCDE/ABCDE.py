import sys
si = sys.stdin.readline
n, m = map(int, si().split())
adj = [[] for _ in range(n)]

for i in range(m):
  x, y = map(int, si().split())
  adj[x].append(y)
  adj[y].append(x)

visited = [False for i in range(n)]

def dfs(i, depth):
  global ans

  if depth == 4:
    print(1)
    sys.exit()
  
  for x in adj[i]:
    if visited[x]:
      continue
    visited[i] = True
    dfs(x, depth+1)
    visited[x] = False

for i in range(n):
  visited[i] = True
  dfs(i,0)
  visited[i] = False

print(0)