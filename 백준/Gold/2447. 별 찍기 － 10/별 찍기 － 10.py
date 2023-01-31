import sys

si = sys.stdin.readline

def starPrint(n):
  
  if n == 1:
    return ['*']

  stars = starPrint(n//3)

  a=[]
  
  for star in stars:
    a.append(star*3)
  for star in stars:
    a.append(star + ' ' * (n//3) + star)
  for star in stars:
    a.append(star*3)

  return a

N = int(si().strip())


print("\n".join(starPrint(N)))