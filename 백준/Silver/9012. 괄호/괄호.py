import sys

si = sys.stdin.readline

T = int(si())

for _ in range(T):
  b = []
  a = list(si().strip())
  isVPS = True

  for i in a:
    if i == "(":
      b.append(i)

    elif i == ")":
      if b:
        b.pop()
      else:
        isVPS = False
        break

  if not b and isVPS:
    print("YES")
  else:
    print("NO")
