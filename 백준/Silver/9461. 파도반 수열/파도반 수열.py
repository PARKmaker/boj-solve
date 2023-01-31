import sys
si = sys.stdin.readline

p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def P(n):
  # print("n=",n)
  for i in range(10, n):
    p[i] = p[i-1] + p[i-5]

  return p[n-1]
  

for _ in range(int(si())):
  n = int(si())

  if n > 10:
    p = p + [0 for _ in range(n - 10)]
    print(P(n))
  
  else:
    print(p[n-1])