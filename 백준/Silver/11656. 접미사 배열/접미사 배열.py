import sys
si = sys.stdin.readline

S = si().rstrip("\n")

a = []

for i in range(len(S)):

  a.append(S[i:])

a.sort()

for i in a:
  print(i)