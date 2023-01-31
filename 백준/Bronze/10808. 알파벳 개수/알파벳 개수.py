import sys
input = sys.stdin.readline

text = input().strip()

a = [0] * 26

for i in text:
  a[ord(i)-ord("a")] += 1

print(*a)