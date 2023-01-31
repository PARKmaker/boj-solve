import sys
si = sys.stdin.readline

n, m = map(int, si().split())
arr = list(sorted(map(int, si().split())))
selected = [0 for _ in range(m)]
used = [0 for _ in range(10001)]

def rec_func(k):
  
  if k == m:
    for i in selected:
      print(arr[i], end=" ")
    print()
    return

  visit = 0
  
  cand = 0 if k == 0 else selected[k-1]

  for i in range(cand, len(arr)):

    if used[i] or visit == arr[i]:
      continue

    selected[k] = i
    used[i] = 1
    visit = arr[i]

    rec_func(k+1)
    selected[k] = 0
    used[i] = 0

rec_func(0)