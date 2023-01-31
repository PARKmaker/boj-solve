import sys
si = sys.stdin.readline

n = int(si())

# n = 5 -> 12345
# n = 15 -> 123456789101112131415
a = [9]
for i in range(1, 10):
  a.append((i+1) * ((10**(i+1)) - (10**i)))

strN = str(n)
digits = len(strN)
ans = 0

ans += digits * (n - 10**(digits-1) + 1)

for i in range(digits-1):
  ans+=a[i]

print(ans)