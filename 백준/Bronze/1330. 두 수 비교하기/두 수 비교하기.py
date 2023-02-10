import sys
si = sys.stdin.readline
a, b = map(int, si().split())

if a > b:
  print(">")
  
elif a < b:
  print("<")

else:
  print("==")