# 연구소 https://www.acmicpc.net/problem/14502

from collections import deque
import queue
import sys
si = sys.stdin.readline

n, m = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(n)]
blank = [(i, j) for i in range(n) for j in range(m) if a[i][j] == 0]
ans = 0


def bfs():
    global ans
    cnt = 0
    visit = [[False]*m for _ in range(n)]
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    queue = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                visit[i][j] = True
                queue.append(i)
                queue.append(j)

    while queue:
        x = queue.popleft()
        y = queue.popleft()
        for dx, dy in dir:
            nx, ny = dx+x, dy+y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[nx][ny] != 0:
                continue
            if visit[nx][ny]:
                continue
            visit[nx][ny] = True
            queue.append(nx)
            queue.append(ny)

    for i in range(n):
        for j in range(m):
            if a[i][j] == 0 and not visit[i][j]:
                cnt += 1

    ans = max(ans, cnt)


def dfs(i, box_selected_cnt):
    if box_selected_cnt == 3:
        bfs()
        return

    if i == len(blank):
        return

    a[blank[i][0]][blank[i][1]] = 1
    dfs(i+1, box_selected_cnt+1)

    a[blank[i][0]][blank[i][1]] = 0
    dfs(i+1, box_selected_cnt)


dfs(0, 0)
print(ans)
