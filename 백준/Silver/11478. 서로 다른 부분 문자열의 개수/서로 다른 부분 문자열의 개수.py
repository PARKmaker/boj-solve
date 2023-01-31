#https://www.acmicpc.net/problem/11478

from sys import stdin
S = stdin.readline().strip()
res = set()

for i in range(len(S)):
  for j in range(i, len(S)):
    res.add(S[i:j+1])

print(len(res))