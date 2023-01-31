import sys
si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
  for j in range(i, -1, -1):
    if a[i] < a[j]:
      dp[i] = max(dp[j]+1, dp[i])
      

print(max(dp))