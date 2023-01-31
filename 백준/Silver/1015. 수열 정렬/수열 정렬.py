import sys

n = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))
listB = [(x, i) for i, x in enumerate(listA)]

listB.sort()

P = [0 for _ in range(n)]
for i in range(n):
    P[listB[i][1]] = i

for i in range(n):
    print(P[i], " ")
