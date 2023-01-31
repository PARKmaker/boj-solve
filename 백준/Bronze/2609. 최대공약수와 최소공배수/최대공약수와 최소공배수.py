import sys

si = sys.stdin.readline

A, B = map(int, si().split())

def func(k, a, b):
  arr = 1
  aa = a
  bb = b

  for i in range(2, k+1):
    while True:
      
      if a % i == 0 and b % i == 0:

        aa = a//i
        bb = b//i
        a = aa
        b = bb
        arr *= i

      else:
        break
    
  print(arr)
  print(arr*aa*bb)

if A == 0 or B == 0:
  print(0)
  print(0)
elif A == 1:
  print(1)
  print(B)
elif B == 1:
  print(1)
  print(A)
else:
  if A <= B:
    func(A, A, B)
  else:
    func(B, A, B)