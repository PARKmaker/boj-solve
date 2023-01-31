import sys
si=sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for _ in range(int(si())):
    A, B = map(int, si().split())

    print(A*B // gcd(A,B))