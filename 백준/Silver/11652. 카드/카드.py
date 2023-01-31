# 카드 https://www.acmicpc.net/problem/11652

import sys

N = int(sys.stdin.readline())

num = []

for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

mode = num[0]
curCnt = 1
modeCnt = 1

for i in range(1, N):
    if num[i] == num[i-1]:
        curCnt += 1
    else:
        curCnt = 1
    if modeCnt < curCnt:
        modeCnt = curCnt
        mode = num[i]

print(mode)
