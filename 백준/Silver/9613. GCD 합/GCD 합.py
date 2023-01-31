import sys
si = sys.stdin.readline

def gcd(a, b):
  while b != 0:
    r = a % b
    a = b
    b = r
  return a

for i in range(int(si())):
  a = list(map(int, si().split()))
  n = len(a)
  res = 0

  for i in range(1, n):
    for j in range(i+1, n):
      
      res += gcd(a[i], a[j])

  print(res)