# 먹을 것인가 먹힐 것인가 https://www.acmicpc.net/problem/7795

import sys
si = sys.stdin.readline


def lower_bound(b, left, right, x):
    result = left - 1
    while left <= right:
        mid = (left + right)//2
        if b[mid] < x:
            result = mid
            left = mid + 1
        else:
            # b[a] >= x:
            right = mid - 1
    return result


def solve():
    b.sort()
    ans = 0
    for x in a:
        ans += lower_bound(b, 0, m-1, x) + 1
    print(ans)


t = int(si())

for _ in range(t):
    n, m = list(map(int, si().split()))
    a = list(map(int, si().split()))
    b = list(map(int, si().split()))
    solve()
