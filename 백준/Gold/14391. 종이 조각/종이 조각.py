import sys
si = sys.stdin.readline
n, m = map(int, si().split())
board = [list(map(int, si().strip())) for _ in range(n)]

ans = 0
def dfs(arr):
  global ans
  tempAns = 0
  if len(arr) == n*m:
    newArr = []
    for i in range(n):
      temp = []
      for cand in range(i*m, i*m + m):
        temp.append(arr[cand])
      newArr.append(temp)
      
    # 가로
    for i in range(n):
      a = 0
      for j in range(m):
        if newArr[i][j] == 0:
          a = a * 10 + board[i][j]
        else:
          tempAns += a
          a = 0
      tempAns += a
      a = 0
    
    for j in range(m):
      b = 0
      for i in range(n):
        if newArr[i][j] == 1:
          b = b * 10 + board[i][j]
        else:
          tempAns += b
          b = 0
      tempAns += b
      b = 0

    ans = max(ans, tempAns)
    return

  else:
    dfs(arr + [0])
    dfs(arr + [1])

dfs([])
print(ans)