import sys
input = sys.stdin.readline

text = input().strip()

a = [-1] * 26

for i in range(len(text)):

  idx = ord(text[i])-ord("a")

  if a[idx] == -1:
    a[idx] = i

print(*a)