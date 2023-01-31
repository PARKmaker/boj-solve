import sys
si = sys.stdin.readline

str = si().strip()
strA = list(str)
strB = []
M = int(si())

def editor(command):
  global N

  if command[0] == "L":
    if not strA:
      return
    else:
      strB.append(strA.pop())

  elif command[0] == "D":
    if not strB:
      return
    else:
      strA.append(strB.pop())
  
  elif command[0] == "B":
    if not strA:
      return
    else:
      strA.pop()

  else:
    strA.append(command[1])

for _ in range(M):
  command = si().strip().split()

  editor(command)

# if strB:
#   for i in range(len(strB)):
#     strA.append(strB.pop())

print("".join(strA+strB[::-1]))