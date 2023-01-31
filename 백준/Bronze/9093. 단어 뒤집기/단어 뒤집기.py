import sys
si = sys.stdin.readline
T = int(si())

for _ in range(T):
  a = si().strip().split()

  a = [w[::-1] for w in a]
  print(" ".join(a))
  # for i in a:
  #   for k in range(len(i), 0, -1):
  #     print(i[k-1], end="")
  #   print(end=" ")