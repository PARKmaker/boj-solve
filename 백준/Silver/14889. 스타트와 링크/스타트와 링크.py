import sys
si = sys.stdin.readline

n = int(si())

people = [[0]] + [[0] + list(map(int,si().split())) for _ in range(n)]
startTeam = [0 for _ in range(n//2)]
team = set([i for i in range(1, n+1)])
ans = 1<<31

def dfs(depth):
  global team, ans

  if startTeam[0] >= (n//2) + 1:
    return

  if depth == n//2:
    linkAns, startAns = 0, 0
    linkTeam = list(team - set(startTeam))

    for i in linkTeam:
      for j in linkTeam:
        if i >= j:
          continue
        linkAns += (people[i][j] + people[j][i])

    for i in startTeam:
      for j in startTeam:
        if i >= j:
          continue
        startAns += (people[i][j] + people[j][i])

    if ans > abs(linkAns - startAns):
      ans = abs(linkAns - startAns)
    return

  else:
    start = 1 if depth == 0 else startTeam[depth-1]+1
    for i in range(start, n+1):
      startTeam[depth] = i
      dfs(depth+1)
      startTeam[depth] = 0

dfs(0)
print(ans)