import sys
si = sys.stdin.readline

n, m = map(int, si().split())
arr = list(map(str, sorted(map(int, si().split()))))
selected = [0 for _ in range(m)]

def rec_func(k):
  
  if k == m:
    for i in selected:
      print(arr[i], end=" ")
    print()
    return
  
  cand = 0 if k == 0 else selected[k-1]
  for i in range(cand, len(arr)):
    
    selected[k] = i
    rec_func(k+1)
    selected[k] = 0

rec_func(0)
