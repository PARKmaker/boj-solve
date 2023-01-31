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

  for i in range(0, len(arr)):
    
    selected[k] = i
    rec_func(k+1)
    selected[k] = 0

rec_func(0)
