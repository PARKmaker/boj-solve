import sys
si = sys.stdin.readline

n = int(si())
arr = [list(map(int, si().split())) for _ in range(n)]

ans = 0

def dfs(day, money):
  global ans
  ans = max(ans, money)

  if day >= n: return

  if day + arr[day][0] <= n:
    dfs(day+arr[day][0], money + arr[day][1])
    dfs(day + 1, money)
  else:
    dfs(day + 1, money)
  return

dfs(0, 0)
print(ans)