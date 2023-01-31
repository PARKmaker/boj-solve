import sys
si = sys.stdin.readline

def dfs(k, arr, depth, visited, selected):
  
  if depth == 6:
    # print(selected)
    for i in selected:
      print(arr[i], end=" ")
    print()
    return
  
  start = 0 if depth == 0 else selected[depth-1]
  for i in range(start, k):
    if visited[i]:
      continue
    
    visited[i] = 1
    selected[depth] = i
    dfs(k, arr, depth+1, visited, selected)
    visited[i] = 0
    selected[depth] = 0

while True:
  
  arr = list(map(int, si().split()))
  k = arr[0]
  arr = arr[1:]
  visited = [0 for _ in range(k)]
  selected = [0 for _ in range(6)]
  
  dfs(k, arr, 0, visited, selected)
  if k == 0:
    break
  print()