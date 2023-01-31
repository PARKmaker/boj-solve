import sys
si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
  
  for j in range(i):

    if a[i] > a[j]:

      dp[i] = max(dp[i], dp[j]+1)
      
maxDp = max(dp)

print(maxDp)

ans = []

for i in range(n-1, -1, -1):
  if dp[i] == maxDp:
    ans.append(a[i])
    maxDp-=1
  
print(*ans[::-1])