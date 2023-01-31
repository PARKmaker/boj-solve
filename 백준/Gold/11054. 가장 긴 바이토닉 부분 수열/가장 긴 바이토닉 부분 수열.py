import sys
si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
a_reverse = a[::-1]

dp = [[1 for _ in range(2)] for _ in range(n)]

for i in range(n):
  for j in range(i):
    
    if a[i] > a[j]:
      dp[i][0] = max(dp[i][0], dp[j][0]+1)

    if a_reverse[i] > a_reverse[j]:
      dp[i][1] = max(dp[i][1], dp[j][1]+1)

result = [0 for _ in range(n)]
for i in range(n):
  result[i] = dp[i][0] + dp[n-i-1][1] - 1

print(max(result))