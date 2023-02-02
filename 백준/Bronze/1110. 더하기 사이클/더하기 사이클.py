N = int(input())
n = N
count = 0

while True:
  
  n10 = N // 10
  n1 = N % 10
  
  if N < 10:
    new_n = N
  else:
    new_n = (n10+n1) % 10
  
  N = n1 * 10 + new_n
  count += 1
  if n == N:
    break

print(count)