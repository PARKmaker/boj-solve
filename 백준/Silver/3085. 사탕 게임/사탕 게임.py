import sys
si = sys.stdin.readline

n = int(si())

def count_board(board):
  maxCnt = 1

  for i in range(n):

    cnt = 1
    for j in range(1,n):
      if board[i][j] == board[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      # maxCnt = max(maxCnt,cnt)

      if cnt > maxCnt:
        maxCnt = cnt
  
    cnt = 1
    for j in range(1,n):
      if board[j][i] == board[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      # maxCnt = max(maxCnt,cnt)

      if cnt > maxCnt:
        maxCnt = cnt

  return maxCnt

  
board = []
for _ in range(n):
  board.append(list(si().rstrip('\n')))
ans = 0

for i in range(n):
  for j in range(n):

    if j+1 < n:
      if board[i][j] == board[i][j+1]:
        continue
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

      temp=count_board(board)
      if temp > ans:
        ans = temp
      # ans.append(count_board(board))
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]


    if i+1 < n:
      if board[i][j] == board[i+1][j]:
        continue
      
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
      # ans.append(count_board(board))
      temp=count_board(board)
      if temp > ans:
        ans = temp
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    

print((ans))