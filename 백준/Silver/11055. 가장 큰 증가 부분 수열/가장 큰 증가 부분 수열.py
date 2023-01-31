import sys
si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
dp = [1 for _ in range(n)]
dp[0] = a[0]

for i in range(1, n):
  for j in range(i):
    if a[i] > a[j]:
      dp[i] = max(dp[i], dp[j]+a[i])
    else:
      dp[i] = max(dp[i], a[i])
print(max(dp))