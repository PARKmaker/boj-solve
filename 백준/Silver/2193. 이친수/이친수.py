import sys
si = sys.stdin.readline

n = int(si())

dp = [[0 for _ in range(2)] for _ in range(n+2)]

dp[1][1] = 1
dp[2][0] = 1

for i in range(3, n+1):
  
  dp[i][0] = sum(dp[i-1])
  dp[i][1] = dp[i-1][0]

print(sum(dp[n]))