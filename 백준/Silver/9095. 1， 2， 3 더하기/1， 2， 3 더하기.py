import sys
si=sys.stdin.readline

for _ in range(int(si())):
    n = int(si())
    
    f = [0 for _ in range(n+3)]
    
    f[1] = 1
    f[2] = 2
    f[3] = 4

    for i in range(4, n+1):
        f[i] = f[i-1] + f[i-2] + f[i-3]

    print(f[n])  
    
