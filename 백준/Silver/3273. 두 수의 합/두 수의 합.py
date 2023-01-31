# 두 수의 합 https://www.acmicpc.net/problem/3273

import sys

si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
x = int(si())
a.sort()

left, right, ans, S = 0, n-1, 0, 0

while left < right:
    if a[left] + a[right] < x:
        left += 1
    elif a[left] + a[right] > x:
        right -= 1
    else:
        ans += 1
        left += 1
        right -= 1

print(ans)
