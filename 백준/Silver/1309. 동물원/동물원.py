import sys
si = sys.stdin.readline

n = int(si())

dp = [[0]] + [[1, 1, 1]] + [[0 for _ in range(3)] for _ in range(n-1)]
mod = 9901
for i in range(2, n+1):
  dp[i][0] = dp[i-1][1] % mod + dp[i-1][2] % mod
  dp[i][1] = dp[i-1][0] % mod + dp[i-1][2] % mod
  dp[i][2] = dp[i-1][0] % mod + dp[i-1][1] % mod + dp[i-1][2] % mod

  # print(dp)

print(sum(dp[n]) % mod)