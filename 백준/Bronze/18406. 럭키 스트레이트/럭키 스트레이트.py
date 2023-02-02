n = input()

s1 = 0
s2 = 0

for i in range(len(n)):
  if i < len(n)//2:
    s1 += int(n[i])
  else:
    s2 += int(n[i])
  
if s1 == s2:
  print("LUCKY")
else:
  print("READY")