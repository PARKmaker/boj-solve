import sys
si = sys.stdin.readline

n, m = map(int, si().split())

arr = list(map(int, si().split()))
used = [0 for _ in range(10001)]
selected = [0 for _ in range(m)]
arr.sort()

def rec_func(k):
  
  if k == m:
    print(*selected)
    return

  for i in arr:
    if used[i]:
      continue
    selected[k] = i
    used[i] = 1
    rec_func(k+1)
    selected[k] = 0
    used[i] = 0


rec_func(0)