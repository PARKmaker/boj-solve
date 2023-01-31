import sys
si = sys.stdin.readline

n = int(si())
team = [list(map(int, input().split())) for i in range(n)]
used = [0 for _ in range(n)] * n

ans = 1 << 31

def solve():
    global ans
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if used[i] and used[j]:
                start += team[i][j]
            elif not used[i] and not used[j]:
                link += team[i][j]
    ans = min(ans, abs(start - link))
    return

def dfs(depth):
    if depth == n:
        solve()
        return
    used[depth] = 1
    dfs(depth + 1)
    used[depth] = 0
    dfs(depth + 1)
dfs(0)

print(ans)