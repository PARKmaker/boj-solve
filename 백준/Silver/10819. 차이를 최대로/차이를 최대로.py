import sys
from itertools import permutations
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
per = list(permutations(arr, n))


answer = 0
for a in per:
  ans = 0
  for i in range(0, n-1):
    ans += abs(a[i] - a[i+1])
  
  if answer < ans:
    answer = ans

print(answer)