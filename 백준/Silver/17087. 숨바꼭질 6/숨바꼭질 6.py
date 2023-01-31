import sys
si = sys.stdin.readline

N, S = map(int, si().split())

def gcd(a,b):
  while b!=0:
    r = a%b
    a = b
    b = r
  return a

a = list(map(int, si().split()))

arr = []

for i in a:
  
  distance = S - i

  if distance == 0:
    continue

  arr.append(abs(distance))

ans = arr[0]

for i in range(1,N):
  ans = gcd(arr[i], ans)

print(ans)