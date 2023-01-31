import sys
si = sys.stdin.readline
from itertools import permutations, combinations

n, m = map(int, si().split())

arr = [i for i in range(1, n+1)]
arr1 = list(permutations(arr, m))

for i in arr1:
    print(*i)