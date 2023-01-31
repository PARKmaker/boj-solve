import sys
si=sys.stdin.readline

N = int(si())
a = list(map(int, si().split()))

answer = [-1] * N
stack = []

stack.append(0)

for i in range(1, N):

  while stack and a[stack[-1]] < a[i]:  
    answer[stack.pop()] = a[i]
  
  stack.append(i)

print(*answer)