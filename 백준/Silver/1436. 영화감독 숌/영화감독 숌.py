import sys
si = sys.stdin.readline

def solve():
  N = int(si())
  
  for i in range(10000666):
    
    if "666" in str(i):
      N -= 1
    
    if N == 0:
      print(i)
      break

solve()
