import sys
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
dp = [arr.copy() for _ in range(2)]
ans = []

for i in range(1, n):
  dp[0][i] = max(dp[0][i], dp[0][i-1] + dp[0][i])
  dp[1][i] = max(dp[0][i-1], dp[1][i-1] + dp[1][i])

print(max(max(dp[0]),max(dp[1])))