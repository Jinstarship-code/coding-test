from collections import deque

n = int(input())
m = int(input())

graph = [[]*m for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in graph:
  i.sort()

def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
    
visited = [False]*(n+1)
bfs(graph,1,visited)

# 숙주인 컴퓨터는 count로 안침.
count = -1
for i in visited:
  if i:
    count+=1
print(count)
  