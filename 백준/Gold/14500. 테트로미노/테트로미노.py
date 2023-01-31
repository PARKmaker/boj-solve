import sys
si = sys.stdin.readline

n, m = map(int, si().split())

tetro = [[[0,0],[0,1],[0,2],[0,3]], [[0,0],[1,0],[2,0],[3,0]], [[0,0],[0,1],[1,0],[1,1]]
        ,[[0,0],[1,0],[2,0],[2,1]], [[0,0],[1,0],[2,0],[2,-1]], [[0,0],[0,1],[1,0],[2,0]],[[0,0],[0,-1],[1,0],[2,0]]
        ,[[0,0],[1,0],[1,1],[2,1]], [[0,0],[1,0],[1,-1],[2,-1]], [[0,0],[0,1],[-1,1],[-1,2]], [[0,0],[0,1],[1,1],[1,2]]
        ,[[0,0],[0,1],[0,2],[1,1]], [[0,0],[0,1],[0,2],[-1,1]], [[0,0],[0,1],[-1,0],[1,0]], [[0,0],[0,1],[-1,1],[1,1]]
        ,[[0,0],[1,0],[1,1],[1,2]], [[0,0],[1,0],[0,1],[0,2]], [[0,0],[0,1],[0,2],[-1,2]], [[0,0],[0,1],[0,2],[1,2]]]

board = []
for _ in range(n):
  board.append(list(map(int, si().split())))

ans = 0
for i in range(n):
  for j in range(m):
    
    maxValue = 0
    for t in tetro:
      value = 0
      for dx, dy in t:
        nx, ny = i+dx, j+dy
        if nx >= n or nx < 0 or ny >= m or ny < 0:
          continue
        value += board[nx][ny]
      
      if maxValue < value:
        maxValue = value

    if ans < maxValue:
        ans = maxValue

print(ans)