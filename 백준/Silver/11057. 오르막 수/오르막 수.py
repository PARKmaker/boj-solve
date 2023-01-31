import sys
si = sys.stdin.readline

n = int(si()) 
mod = 10007
dp = [[0 for _ in range(10)] for _ in range(n+2)]

for i in range(10):
  dp[1][i] = 1
  dp[2][i] = 10 - i

for i in range(3, n+1):
  for j in range(10):

    for k in range(j, 10):
      
      dp[i][j] += dp[i-1][k]

print(sum(dp[n]) % mod)