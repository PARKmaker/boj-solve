import sys
si = sys.stdin.readline

n = int(si())

dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
  dp[1][i] = 1

for i in range(2, n+1):
  for k in range(10):

    if k == 0:
      dp[i][k] = dp[i-1][1]
    
    elif k == 9:
      dp[i][k] = dp[i-1][8]
    
    else:
      dp[i][k] = dp[i-1][k-1] + dp[i-1][k+1]

# print(dp[1])
print(sum(dp[n]) % 1000000000)