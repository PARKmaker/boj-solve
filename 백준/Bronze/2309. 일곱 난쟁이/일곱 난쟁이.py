import sys
si = sys.stdin.readline

arr = []
length = 0
while True:
  
  n = si().rstrip('\n')

  if not n:
    break
  
  length += int(n)
  arr.append(int(n))

arr.sort()

for i in range(9):
  currLength = length
  currLength -= arr[i]

  for cand in range(9):
    if i == cand:
      continue
    currLength -= arr[cand]

    if currLength == 100:
      arr.pop(i)
      arr.pop(cand-1)
      break
    
    currLength += arr[cand]
  
  if currLength == 100:
    break

for i in arr:
  print(i)