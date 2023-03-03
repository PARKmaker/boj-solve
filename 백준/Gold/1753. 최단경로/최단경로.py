import heapq, sys
si = sys.stdin.readline
INF = 1<<31

v, e = map(int, si().split())
start = int(si())
graph = [[] for _ in range(v+1)]
visited = [0 for _ in range(v+1)]
distance = [INF for _ in range(v+1)]

for _ in range(e):
  a, b, cost = map(int, si().split())
  graph[a].append((b, cost))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    
    for next_node in graph[node]:
      cost = distance[node] + next_node[1]
      
      if cost < distance[next_node[0]]:
        distance[next_node[0]] = cost
        heapq.heappush(q, (cost, next_node[0]))
        
dijkstra(start)

for i in range(1, v+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])