import sys
si = sys.stdin.readline

n = int(si())
a = []

max_cnt = [[] for _ in range(500000)]

for _ in range(n):
  a.append(int(si()))
a.sort()

print(round(sum(a)/n))
print(a[int(len(a)/2)])

cnt = 0
cnt_max = 0
m = a[0]

for i in range(len(a)):
  if m == a[i]:
    cnt+=1
    max_cnt[cnt].append(a[i])

  else:
    cnt = 1
    m = a[i]
    max_cnt[cnt].append(a[i])

  cnt_max = max(cnt_max, cnt)

if len(max_cnt[cnt_max]) > 1:
  print(max_cnt[cnt_max][1])
else:
  print(max_cnt[cnt_max][0])

print(a[-1]-a[0])