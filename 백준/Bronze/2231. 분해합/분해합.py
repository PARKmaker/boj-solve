import sys
si=sys.stdin.readline

N = int(si())

Min = 1000001
sum = 0

def f(k):
  global Min, sum

  k1 = k-1
  while k1:
    
    strk = str(k1)
    res = k1
    # print("k1==",k1)
    for i in range(len(strk)):
      res += int(strk[i])
      # print("res=",res)
    
    if res == k:
      Min = min(k1, Min)
    k1-=1
f(N)

if Min == 1000001:
  print(0)
else:
  print(Min)