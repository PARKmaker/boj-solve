import sys
from collections import Counter
si=sys.stdin.readline

N = int(si())
a = list(map(int, si().split()))

answer = [-1] * N
stack = [0]

setA = set(a)
funcA = Counter(a)
# for i in setA:
#   funcA.append(a.count(i))

# stack.append(0)

for i in range(1, N):

  while stack and funcA[a[stack[-1]]] < funcA[a[i]]:
    answer[stack.pop()] = a[i]
  
  stack.append(i)

print(*answer)