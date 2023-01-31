import sys
si = sys.stdin.readline

n, s = map(int,si().split())
arr = list(map(int, si().split()))
ans = 0

def dfs(depth, value):
  global res, ans

  if depth == n:
    if value == s:
      ans +=1

  else:
    dfs(depth+1, value + arr[depth])
    dfs(depth+1, value)

dfs(0, 0)
if s == 0:
  print(ans-1)
else:
  print(ans)