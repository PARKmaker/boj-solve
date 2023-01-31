import sys
si = sys.stdin.readline

currCh = 100
n = int(si())
m = int(si())
brokenBtn = list(map(int, si().split()))
cnt = 0
btn = []
for idx in range(10):
  if idx not in brokenBtn:
    btn.append(idx)

click = abs(100 - n)

# if m == 0:
#   click = len(str(n))
# else:
#   click = abs(n - 100)

strN = str(n)
minDiff = 1<<31

for i in range(1000001):
  possible = True
  s = str(i)
  
  for j in range(len(s)):
    if int(s[j]) not in btn:
      # print(f's={s}')
      possible = False
      break
  
  if not possible: continue
  else:
    # print(f'i={i}, abs = {abs(n-i)}')
    if abs(n - i) < minDiff:
      minDiff = abs(n - i) + len(s)
    
    click = min(click, minDiff)

print(click)