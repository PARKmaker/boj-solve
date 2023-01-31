import sys
si = sys.stdin.readline

a = []
def stack(operater):
  
  if operater == "push":
    a.append(oper[1])
  
  elif operater == "pop":
    if len(a) == 0:
      print(-1)
    else:
      print(a[len(a)-1])
      a.pop()
  
  elif operater == "size":
    print(len(a))
  
  elif operater == "empty":
    if len(a) == 0:
      print(1)
    else:
      print(0)

  else:
    if len(a) == 0:
      print(-1)
    else:
      print(a[len(a)-1])

N = int(si())

for _ in range(N):
  oper = si().split()
  
  stack(oper[0])