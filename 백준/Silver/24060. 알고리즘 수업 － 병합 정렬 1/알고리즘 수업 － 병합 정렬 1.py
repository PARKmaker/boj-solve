import sys

si = sys.stdin.readline

def merge_sort(A, p, r):
  if p < r:
    mid = (p + r) // 2
    merge_sort(A, p, mid)
    merge_sort(A, mid+1, r)
    merge(A, p, mid, r)

def merge(A, p, q, r):

  global count, result
  i = p
  j = q+1

  temp = []
  while i <= q and j <= r:
    if A[i] <= A[j]:
      temp.append(A[i])
      i+=1
    else:
      temp.append(A[j])
      j+=1
  
  while i <= q:
    temp.append(A[i])
    i+=1

  while j <= r:
    temp.append(A[j])
    j+=1

  i, t = p, 0

  while i <= r:
    A[i] = temp[t]
    count += 1
    if count == K:
      result = A[i]
      break;
    i += 1
    t += 1

N, K = map(int, si().split())
a = list(map(int,input().split()))
count = 0
result = -1
merge_sort(a, 0, N-1)
print(result)