import sys

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
vst1 = [[False] * 9 for _ in range(9)]
vst2 = [[False] * 9 for _ in range(9)]
vst3 = [[False] * 9 for _ in range(9)]

def box(i,j):
  return i//3 * 3 + j//3

for i in range(9):
  for j in range(9):
    if matrix[i][j]:
      vst1[i][matrix[i][j] - 1] = True
      vst2[j][matrix[i][j] - 1] = True
      vst3[box(i,j)][matrix[i][j] - 1] = True

def back(i,j):
  if i == 9:
    return True

  if matrix[i][j]:
    return back(i + (j + 1)//9, (j+1) % 9)
    
  
  for k in range(9):
    if vst1[i][k] or vst2[j][k] or vst3[box(i,j)][k]:
      continue
    matrix[i][j] = k+1
    vst1[i][k] = vst2[j][k] = vst3[box(i,j)][k] = True
    if back(i + (j + 1)//9, (j+1) % 9):
      return True
    matrix[i][j] = 0
    vst1[i][k] = vst2[j][k] = vst3[box(i,j)][k] = False
  return False

back(0,0)
for x in matrix:
  print(*x)