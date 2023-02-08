import sys
si = sys.stdin.readline
sys.setrecursionlimit(1000001)
n , m = map(int,si().split())
board = [si().strip() for _ in range(n)]

visit = [[0 for _ in range(m)] for _ in range(n)]
dir = [[0, 1], [1,0], [0, -1], [-1, 0]]
ans = "No"

def dfs(x, y):
  global i, j, ans
  visit[x][y] = 1
  
  if visit[i][j+1] and x-1 == i and y == j:
    print("Yes")
    exit(0)
  
  else:
    for dx, dy in dir:
      nx, ny = dx + x, dy + y
      
      if nx >= n or ny >= m or nx < 0 or ny < 0:
        continue
      
      if visit[nx][ny]:
        continue
      
      if board[nx][ny] != board[x][y]:
        continue
      
      visit[nx][ny] = 1
      dfs(nx, ny)
      visit[nx][ny] = 0
      
for i in range(n-1):
    for j in range(m-1):
      if visit[i][j]:
        continue
      
      if ans == "No":
        visit[i][j] = 1
        dfs(i, j)
        visit[i][j] = 0
      else:
        break
    
print(ans)