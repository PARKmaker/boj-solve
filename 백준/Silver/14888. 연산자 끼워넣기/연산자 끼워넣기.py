import sys
si = sys.stdin.readline

N = int(si())
A = list(map(int, si().split()))
operater = list(map(int, si().split()))

min = 1e9
max = -1e9

def calc(value1, value2, operater):
  if operater == 0:
    return value1 + value2
  if operater == 1:
    return value1 - value2
  if operater == 2:
    return value1 * value2
  if operater == 3:
    if value1 < 0:
      return -((-value1) // value2)
    else:
      return value1 // value2

def f(k, value):
  
  if k == N-1:
    global min, max
    min = min if min < value else value
    max = max if max > value else value

  for cand in range(4):
    global operators
    if operater[cand] >= 1:
      operater[cand] -= 1
      f(k+1, calc(value, A[k+1], cand))
      operater[cand] += 1


f(0, A[0])

print(max)
print(min)