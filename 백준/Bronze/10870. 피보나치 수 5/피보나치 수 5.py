import sys

si = sys.stdin.readline

n = int(si())

def f(n):
    res = n
    if n>=2:
        res = f(n-1) + f(n-2)

    return res

print(f(n))