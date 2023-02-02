import sys
si = sys.stdin.readline

n = int(si())
board = [list(map(int, si().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]

def dfs(x, y):
  global group_cnt, groups
  group_cnt+=1
  visited[x][y] = 1

  for dx, dy in dir:
    nx, ny = dx+x, dy+y
    if nx >= n or ny >= n or nx < 0 or ny < 0:
      continue
    if visited[nx][ny]: continue
    if board[nx][ny] == 0: continue 
    dfs(nx, ny)
  return

group_cnt = 0
groups = []
for i in range(n):
  for j in range(n):
    if board[i][j]==0 or visited[i][j]:
      continue
    group_cnt = 0
    dfs(i, j)
    groups.append(group_cnt)

groups.sort()
print(len(groups))
for g in groups:
    print(g)