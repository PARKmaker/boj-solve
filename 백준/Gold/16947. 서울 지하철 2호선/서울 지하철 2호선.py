import sys
from collections import deque
sys.setrecursionlimit(10**9)
si = sys.stdin.readline

n = int(si())
adj = [[] for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(n):
  x, y = map(int, si().split())
  adj[x].append(y)
  adj[y].append(x)

def dfs(x, cnt):
  
  if visit[x]:
    if cnt - dist[x] >= 3:
      return x
    else:
      return -1
    
  visit[x] = 1
  dist[x] = cnt
  
  for y in adj[x]:
    start = dfs(y, cnt + 1)
    
    if start != -1:
      visit[x] = 2
      if x == start:
        return -1
      else:
        return start
  
  return -1

def bfs():
  q = deque()
  for i in range(1, n+1):
    if visit[i] == 2:
      q.append(i)
      dist[i] = 0
    else:
      dist[i] = -1

  while q:
    x = q.popleft()
    for y in adj[x]:
      if dist[y] == -1:
        q.append(y)
        dist[y] = dist[x] + 1

dfs(1,0)
bfs()
print(*dist[1:])
