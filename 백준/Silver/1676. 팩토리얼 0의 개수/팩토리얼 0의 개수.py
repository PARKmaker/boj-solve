import sys

si = sys.stdin.readline

n = int(si())

def factorial(x):
    res = 1
    if x > 0: 
        res = x * factorial(x-1)

    return res

cnt = 0
ans = 0

num = factorial(n)
S = str(num)

for i in range(len(S)-1, 0, -1):

    if S[i] == "0":
        
        ans += 1
    
    if S[i] != "0":
        break

print(ans)