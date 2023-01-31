import sys

si = sys.stdin.readline

N = int(si())

a = []

for _ in range(N):
  a.append(list(map(int, si().split())))

for i in a:
  rank = 1

  for j in a:
    if i[0] < j[0] and i[1]<j[1]:
      rank += 1

  print(rank, end = " ")