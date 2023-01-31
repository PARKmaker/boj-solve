# https://www.acmicpc.net/problem/9184

import sys
si = sys.stdin.readline

dic = {}

def w(a, b, c):

  if (a,b,c) in dic:
    return dic[(a,b,c)]

  elif a<=0 or b<=0 or c<=0:
    return 1
  
  elif a > 20 or b > 20 or c > 20:
    return w(20,20,20)
  
  elif a < b < c:
    num = w(a,b,c-1) + w(a, b-1, c-1) - w(a,b-1,c)
    dic[(a,b,c)] = num
    return num
  
  else:
    num = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    dic[(a,b,c)] = num
    return num

while True:

  a, b, c  = map(int, si().split())
  if a == -1 and b == -1 and c == -1:
    break

  print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))

# print(a[1][1][1])