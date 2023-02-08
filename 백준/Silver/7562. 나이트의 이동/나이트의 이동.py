import sys
from collections import deque
si = sys.stdin.readline

dir = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

for i in range(int(si())):
  l = int(si())
  currX, currY = map(int, si().split())
  targetX, targetY = map(int, si().split())
  dist = [[-1 for i in range(l)] for _ in range(l)]
  dist[currX][currY] = 0
  
  if currX == targetX and currY == targetY:
    print(0)
  
  else:
    q = deque()
    q.append(currX)
    q.append(currY)
    
    while q:
      x = q.popleft()
      y = q.popleft()
      
      for dx, dy in dir:
        nx, ny = dx + x, dy + y
        # print(f'nx = {nx}, ny = {ny}')
        
        if nx >= l or ny >= l or nx < 0 or ny < 0:
          continue
        if dist[nx][ny] != -1:
          continue
        dist[nx][ny] = dist[x][y] + 1
        if targetX == nx and targetY == ny:
          print(dist[nx][ny])
          break
        
        q.append(nx)
        q.append(ny)