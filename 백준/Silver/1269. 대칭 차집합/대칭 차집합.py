import sys
si = sys.stdin.readline

A, B = map(int, si().split())

aArr = list(map(int, si().split()))
bArr = list(map(int, si().split()))

b = {}
for i in bArr:
  b[i] = 1

cnt = 0
for i in aArr:
  if i in b:
    cnt+= 1
print(len(aArr) + len(bArr) - (cnt * 2))