import sys
si = sys.stdin.readline

n = int(si())
arr = [[0, 0, 0]]
maxInt = 1<<31
ans = maxInt

for _ in range(n):
  arr.append(list(map(int, si().split())))

for color in range(3):
  dp = [[0 for _ in range(3)] for _ in range(n+1)]
  dp[1] = [maxInt, maxInt, maxInt]
  dp[1][color] = arr[1][color]

  for j in range(2, n+1):
    dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + arr[j][0]
    dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + arr[j][1]
    dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + arr[j][2]
  
  dp[n][color] = maxInt
  ans = min(ans, min(dp[n]))

print(ans)