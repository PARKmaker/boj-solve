import sys
si = sys.stdin.readline
mod = 1000000009

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = dp[i-1] % mod + dp[i-2] % mod + dp[i-3] % mod

for _ in range(int(si())):
  n = int(si())

  print(dp[n] % mod)  