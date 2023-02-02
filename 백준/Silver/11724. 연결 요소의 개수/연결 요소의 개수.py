import sys
si = sys.stdin.readline
sys.setrecursionlimit(1000001)

n, m = map(int, si().split())
adj = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]

for i in range(m):
    x, y = map(int, si().split())
    adj[x].append(y)
    adj[y].append(x)
    
for i in range(1, n+1):
    adj[i].sort()
    
ans = 0
def dfs(depth):
    visited[depth] = 1

    for x in adj[depth]:
        if visited[x]:
            continue
        dfs(x)
        
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        ans += 1
    
print(ans)