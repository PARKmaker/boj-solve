import sys
si = sys.stdin.readline

l, c = map(int, si().split())
arr = sorted(si().strip().split())

vowelArr = ["a","e","i","o","u"]
used = [0 for _ in range(c)]
selected = [0 for _ in range(l)]

def dfs(depth):
  
  if depth == l:
    consonant, vowel = 0, 0
    ans = []

    for i in selected:
      if arr[i] in vowelArr:
        vowel += 1
      else:
        consonant += 1
      ans.append(arr[i])
    
    if vowel >= 1 and consonant >= 2:
      print(*ans, sep="")
    return

  cand = 0 if depth == 0 else selected[depth-1]
  for i in range(cand, c):
    if used[i]:
      continue
    
    used[i] = 1
    selected[depth] = i
    dfs(depth+1)
    used[i] = 0
    selected[depth] = 0

dfs(0)