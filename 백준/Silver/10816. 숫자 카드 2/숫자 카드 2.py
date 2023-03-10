import sys
si = sys.stdin.readline
n = int(si())
a = sorted(list(map(int, si().split())))

m = int(si())
b = list(map(int, si().split()))

def lower(a, l, r, x):
  res = r+1

  while l<=r:
    mid = (l+r) // 2
    
    if a[mid] >= x:
      res = mid
      r = mid - 1
    else:
      l = mid + 1

  return res

def upper(a, l, r, x):
  res = r+1

  while l<=r:
    mid = (l+r) // 2
    
    if a[mid] > x:
      res = mid
      r = mid - 1
    else:
      l = mid + 1

  return res

for x in b:
  print(upper(a, 0, n-1, x) - lower(a, 0, m-1, x), end=' ')