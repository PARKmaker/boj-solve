import sys
si = sys.stdin.readline

m = int(si())
s = set()

for i in range(m):
  cmd = si().strip().split()
  
  if len(cmd) == 1:
    if cmd[0] == "all":
      s = set([i for i in range(1, 21)])
    else:
      s = set()

  else:
    command, x = cmd[0], cmd[1]
    x = int(x)
    if command == "add":
      s.add(x)
  
    elif command == "remove":
      s.discard(x)

    elif command == "check":
      if x in s:
        print(1)
      else:
        print(0)

    elif command == "toggle":
      if x in s:
        s.discard(x)
      else:
        s.add(x)