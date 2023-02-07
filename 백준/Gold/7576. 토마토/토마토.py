import sys
from collections import deque
si = sys.stdin.readline

m, n = map(int, si().split())
tomato = [list(map(int, si().split())) for i in range(n)]

dist = [[-1 for _ in range(m)] for _ in range(n)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]

q = deque()
for i in range(n):
  for j in range(m):
    if tomato[i][j] == 1:
      dist[i][j] = 0
      q.append(i)
      q.append(j)
    
while q:
  x = q.popleft()
  y = q.popleft()
  
  for dx, dy in dir:
    nx, ny = dx+x, dy+y
    if nx >= n or ny >= m or nx < 0 or ny < 0:
      continue
    if dist[nx][ny] != -1:
      continue
    if tomato[nx][ny] == -1:
      continue
    
    q.append(nx)
    q.append(ny)
    dist[nx][ny] = dist[x][y] + 1
    
ans = 0

for i in range(n):
  for j in range(m):
    if tomato[i][j] == -1:
      continue
    if dist[i][j] == -1:
      ans = -1
    if ans == -1:
      continue
    
    ans = max(ans, dist[i][j])
    
print(ans)