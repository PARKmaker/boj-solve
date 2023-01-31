import sys
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
possible = False

for i in range(n-1, 0, -1):
  if arr[i] < arr[i-1]:
    idx1, idx2 = i-1, i

    for j in range(n-1, -1, -1):
      if arr[j] < arr[idx1]:
        arr[j], arr[idx1] = arr[idx1], arr[j]
        possible = True
        break
    
  if possible:
    arr = arr[:idx2] + sorted(arr[idx2:], reverse=True)
    print(*arr)
    break

if not possible:
  print(-1)