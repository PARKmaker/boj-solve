import sys
si = sys.stdin.readline

n = 1000000

sieve = [1] * (n+1)

m = int(n**0.5)

for i in range(2, m+1):
  if sieve:
    for j in range(i+i, n, i):
      sieve[j] = 0

while True:
  
  N = int(si())

  if N == 0:
    break
  
  possible = False

  for i in range(3, len(sieve)):
    
    if sieve[i] and sieve[N-i]:
      print("{} = {} + {}".format(N, i, N-i))
      possible = True
      break
    
  if not possible:
    print("Goldbach's conjecture is wrong.")