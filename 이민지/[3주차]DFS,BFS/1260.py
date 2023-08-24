import sys
from collections import deque
input = sys.stdin.readline

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# bfs
def bfs(graph, s, visited):
    q = deque([s])
    visited[s] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
            

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
dfs_visited = [False]*(n+1) # dfs 방문
bfs_visited = [False]*(n+1) # bfs 방문
for _ in range(m):
    a,b = map(int,input().split())
    # 양방향 연결
    # 정점 번호가 작은 것을 먼저 방문해야하므로 오름차순 정렬
    graph[a].append(b)  
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

# 답 출력
dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)