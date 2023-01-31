import sys
s = sys.stdin.readline().strip()

a = []
res = 0

for i in range(len(s)):
  
  if s[i] == "(":
    a.append(s[i])
  
  elif s[i] == ")":
    
    if s[i-1] == "(":
      a.pop()
      res += len(a)
    
    else:
      a.pop()
      res += 1

print(res)