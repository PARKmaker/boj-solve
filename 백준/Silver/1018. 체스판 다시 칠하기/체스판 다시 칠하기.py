import sys

si = sys.stdin.readline

N, M = map(int, si().split())

orign = []

Min = 1<<31

for _ in range(N):
  orign.append(si().strip())

cnt=[]

for x in range(0, N-7):
  for y in range(0, M-7):

    w = 0
    b = 0
    
    for i in range(x, x + 8):
      for j in range(y, y + 8):
        if (i+j) % 2 == 0:
          if orign[i][j] == "B":
            b += 1
          if orign[i][j] == "W":
            w += 1

        else:
          if orign[i][j] == "B":
            w += 1
          if orign[i][j] == "W":
            b += 1
            

    cnt.append(min(w,b))


print(min(cnt))
