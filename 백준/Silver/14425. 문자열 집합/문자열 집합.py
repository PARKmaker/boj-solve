import sys
si = sys.stdin.readline

N, M = map(int, si().split())

S = sorted([si().strip() for _ in range(N)])
check = sorted([si().strip() for _ in range(M)])

cnt = 0

def solve(S, l, r, x):

  while l <= r:
    mid = (l+r)//2

    if S[mid] == x:
      return True
    elif S[mid] < x:
      l = mid + 1
    else:
      r = mid - 1

  return False

for i in check:
  if solve(S, 0, N-1, i):
    cnt += 1

print(cnt)