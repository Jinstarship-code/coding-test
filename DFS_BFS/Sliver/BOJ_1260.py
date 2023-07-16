from collections import deque

n,m,v = map(int,input().split())

# n*m 배열생성
graph = [[]*m for _ in range(n+1)]

# 방문처리
visited = [False] * (n+1)

# 도르는 양방향이다.
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph,v,visited):
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

def bfs(graph,start,visited):
  queue = deque([start]) # queue안에 시작원소를 넣고.
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 도시 -> 도시의 번호를 오름차순으로 정렬
for i in graph:
  i.sort()

dfs(graph,v,visited)
print(end='\n')
visited = [False]*(n+1)
bfs(graph,v,visited)
        