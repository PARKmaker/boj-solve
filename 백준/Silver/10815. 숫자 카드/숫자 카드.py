import sys
si = sys.stdin.readline

N = int(si())
aN = set(list(map(int, si().split())))
M = int(si())
aM = list(map(int, si().split()))

solve =[] 
for i in aM:
  if i in aN:
    solve.append(1)
  else:
    solve.append(0)

print(*solve)