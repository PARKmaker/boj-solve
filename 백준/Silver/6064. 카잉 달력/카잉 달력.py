import sys
si = sys.stdin.readline

def solve(m, n, x, y):
  year = x
  while year <= m * n:
    
    year_x = year - x
    year_y = year - y

    # print(f'year = {year}, year_x = {year_x}, year_y = {year_y}')
    if year_x % m == 0 and year_y % n == 0:
      return year

    year += m
    
  return -1


for i in range(int(si())):
  m, n, x, y = map(int, si().split())
  print(solve(m, n, x, y))