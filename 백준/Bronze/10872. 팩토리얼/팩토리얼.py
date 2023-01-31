import sys

si = sys.stdin.readline

n = int(si())

def factorial(x):
    res = 1
    if x > 0: 
        res = x * factorial(x-1)

    return res

    

print(factorial(n))