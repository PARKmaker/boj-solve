# List of Unique Numbers https://www.acmicpc.net/problem/13144


import sys

si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))

right = -1
cnt = [0] * 100002
ans = 0


for left in range(n):
    while right+1 < n and cnt[a[right+1]] == 0:
        right += 1
        cnt[a[right]] += 1

    ans += right - left + 1
    cnt[a[left]] -= 1

print(ans)
