import sys
si = sys.stdin.readline

N = int(si())

stack = []
answer = []
j = False
cur = 1

for i in range(N):
  n = int(si())

  while cur<=n:
    stack.append(cur)
    answer.append("+")
    cur+=1
  # print(stack)
  if stack[-1] == n:
    stack.pop()
    answer.append("-")

  else:
    print("NO")
    j = True
    break

if not j:
  for i in answer:
    print(i)