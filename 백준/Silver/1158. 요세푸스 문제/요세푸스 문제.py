import sys
si=sys.stdin.readline

N, K = map(int, si().split())

a = []
for i in range(1, N+1):
  a.append(i)

result = []
n = 0

for i in range(N):
  n += K - 1
  if n >= len(a):
    n = n % len(a)
  
  result.append(str(a.pop(n)))

print("{0}".format(result).replace("'","").replace("[","<").replace("]",">"))

