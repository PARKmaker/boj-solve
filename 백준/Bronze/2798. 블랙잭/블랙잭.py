import sys

si = sys.stdin.readline

N, M = list(map(int, si().split()))
a = list(map(int, si().split()))
sum = 0
res = 0

def f(k,n):
  global sum, res
  if k == 4:
    res = max(res, sum)
    # print("res=",res)
    return

  for i in range(n, N):
    sum += a[i]
    if sum > M:
      sum -= a[i]
      continue

    # print("1 k={0},n={1},i={2},sum={3},a[i]={4}".format(k,n,i,sum,a[i]))
    f(k+1, i+1)
    sum -= a[i]



f(1, 0)
print(res)
