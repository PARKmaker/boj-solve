import sys
si = sys.stdin.readline

# arr = list(map(int, si().split()))
E, S, M = map(int, si().split())
e,s,m = 1, 1, 1
cnt = 1

if E == 1 and S == 1 and M == 1:
  print(cnt)

else:
  while True:
    e += 1
    if e >= 16:
      e = 1

    s += 1
    if s >= 29:
      s = 1
      
    m += 1
    if m >= 20:
      m = 1
    
    cnt += 1
    
    if e == E and s == S and m == M:
      print(cnt)
      break
# print(a)
