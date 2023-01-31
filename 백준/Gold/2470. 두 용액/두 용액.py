# 두 용액 https://www.acmicpc.net/problem/2470

import sys

n = int(sys.stdin.readline())

a = sorted(list(map(int, sys.stdin.readline().split())))


def lower_bound(a, left, right, x):
    result = right + 1
    while left <= right:
        mid = (left+right)//2
        if a[mid] >= x:
            result = mid
            right = mid-1
        else:
            left = mid+1
    return result


best_sum = sys.maxsize

v1, v2 = 0, 0

for left in range(n-1):
    candidate = lower_bound(a, left+1, n-1, -a[left])
    if left < candidate-1 and abs(a[left]+a[candidate-1]) < best_sum:
        best_sum = abs(a[left]+a[candidate-1])
        v1, v2 = a[left], a[candidate-1]
    if candidate < n and abs(a[left] + a[candidate]) < best_sum:
        best_sum = abs(a[left]+a[candidate])
        v1, v2 = a[left], a[candidate]

print(v1, v2)
