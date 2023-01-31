import sys
si = sys.stdin.readline

k = int(si())
arr = si().strip().split()
used = [0 for _ in range(10)]

minAns = ""
maxAns = ""
def compareble(prev, curr, sign):
  if sign == "<":
    return prev < curr
  else:
    return prev > curr

def dfs(depth, ans):
  global minAns, maxAns

  if depth == k+1:
    if len(minAns) == 0:
      minAns = ans
    else:
      maxAns = ans
    return
      
  for i in range(10):
    if used[i] == 0:
      if depth == 0 or compareble(ans[-1], str(i), arr[depth-1]):
        used[i] = 1
        dfs(depth+1, ans+str(i))
        used[i] = 0

dfs(0, "")
print(maxAns)
print(minAns)