import sys
si = sys.stdin.readline
sys.setrecursionlimit(1000001)

def dfs(x, y):
  global cnt
  cnt += 1
  visit[x][y] = 1
  
  for dx, dy in dir:
    nx, ny = dx+x, dy+y
    if nx >= h or ny >= w or nx < 0 or ny < 0:
      continue
    if visit[nx][ny]:
      continue
    if board[nx][ny] == 0:
      continue
    
    dfs(nx, ny)

while True:
  cnt = 0
  groups = []
  dir = [[1,0], [1, 1], [1, -1], [-1, 1], [0,1], [-1, 0], [0, -1], [-1, -1]]
  w, h = map(int, si().split())
  visit = [[0 for i in range(w)] for i in range(h)]
  
  if w == 0 and h == 0:
    break
  
  board = [list(map(int, si().split())) for _ in range(h)]
  
  for i in range(h):
    for j in range(w):
        if visit[i][j] or board[i][j] == 0:
          continue
        
        dfs(i, j)
        groups.append(cnt)
        
  print(len(groups))