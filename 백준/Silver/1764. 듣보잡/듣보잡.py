import sys
si = sys.stdin.readline

dic = {}
N, M = map(int, si().split())

for _ in range(N):
  a = si().strip()
  dic[a] = 1

arr =[]
for _ in range(M):
  b = si().strip()

  if b in dic:
    arr.append(b)
  
print(len(arr))
arr.sort()
for i in arr:
  print(i)