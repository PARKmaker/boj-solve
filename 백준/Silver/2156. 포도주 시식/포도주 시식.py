import sys
si = sys.stdin.readline

n = int(si())

# a=[]
# for _ in range(n):
#   a.append(int(si()))

dp = [[0 for _ in range(3)] for _ in range(n+3)]

for i in range(3, n+3):
  cand = int(si())
  dp[i][0] = cand + max(dp[i-3][0], dp[i-3][1], dp[i-3][2])
  dp[i][1] = cand + max(dp[i-2][0], dp[i-2][1], dp[i-2][2])
  dp[i][2] = cand + max(dp[i-1][0], dp[i-1][1])

# print(max(max(dp)))
print(max(max(dp)))