import sys
si = sys.stdin.readline


for _ in range(int(si())):
  
  n = int(si())
  a=[]
  for _ in range(2):
    a.append(list(map(int, si().split())))
  a.append([0] * n)

  dp = [[0 for _ in range(n)] for _ in range(3)]

  for i in range(2):
    dp[i][0] = a[i][0]
  
  for i in range(1, n):
    dp[0][i] += max(dp[1][i-1], dp[2][i-1]) + a[0][i]
    dp[1][i] += max(dp[0][i-1], dp[2][i-1]) + a[1][i]
    dp[2][i] += max(dp[0][i-1], dp[1][i-1]) + a[2][i]

  print(max(max(dp[0]),max(dp[1]),max(dp[2])))