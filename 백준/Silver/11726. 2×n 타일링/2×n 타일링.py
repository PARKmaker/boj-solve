import sys
si = sys.stdin.readline

n = int(si())

a = [0 for _ in range(n+2)]

a[1] = 1
a[2] = 2

for i in range(3, n+2):

  a[i] = (a[i-1] + a[i-2]) % 10007

print(a[n])