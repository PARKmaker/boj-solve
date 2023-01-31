import sys
si = sys.stdin.readline

N, M = map(int, si().split())

aInt = {}
aStr = {}

for i in range(1, N+1):
  a = si().strip()
  aInt[i] = a
  aStr[a] = i

aM = [si().strip() for _ in range(M)]

for i in aM:
  try:
    print(aInt[int(i)])

  except:
    print(aStr[i])
    