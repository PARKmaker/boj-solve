import sys
si = sys.stdin.readline

N = int(si())
q = []

def queue(command):
  global q
  if command[0] == "push":
    q.append(command[1])
  
  elif command[0] == "pop":
    if not q:
      print(-1)
    else:
      print(q[0])
      q = q[1:]
  
  elif command[0] == "size":
    print(len(q))
  
  elif command[0] == "empty":
    if len(q) == 0:
      print(1)
    else:
      print(0)

  elif command[0] == "front":
    if not q:
      print(-1)
    else:
      print(q[0])
  
  else:
    if not q:
      print(-1)
    else:
      print(q[-1])

for _ in range(N):
  command = si().strip().split()
  # print(command)
  queue(command)