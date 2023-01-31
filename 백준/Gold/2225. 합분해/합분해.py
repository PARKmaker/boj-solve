import sys
si = sys.stdin.readline

n, k = map(int, si().split())

mod = 1000000000

dp = [[1 for _ in range(k+2)]] + [[0 for _ in range(k+2)] for _ in range(n)]

for i in range(n+1):
  dp[i][1] = 1

for i in range(k+1):
  dp[1][i] = i

for i in range(2, n+1):
  dp[i][2] = i+1

for i in range(2, n+1):
  for j in range(3, k+1):
    # print(f'i = {i}, j = {j}')

    for cand in range(i, -1, -1):
      dp[i][j] += dp[cand][j-1]
#       print(f'cand = {cand}, dp[{cand}][{j-1}] = {dp[cand][j-1]}, dp[{i}][{j}] = {dp[i][j]}')
      
# print(dp)

print(dp[n][k] % mod)