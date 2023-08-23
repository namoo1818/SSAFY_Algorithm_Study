# bfs 시도하다 막힘

from collections import deque

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n):
            if visited_bfs[i]==0 and lst[v][i]==1:
                queue.append(i)
                visited_bfs[i] = 1

name = [1, 2, 3, 4]
n, m, v=map(int, input().split()) # n은 정점, m은 간선, v는 탐색 시작할 정점 번호
visited_dfs = [0]*m
visited_bfs = [0] * m
lst = [[] for _ in range(m)]

for i in range(m):
    s, e=map(int, input().split())
    lst[s].append(e)        # 인접 리스트 입력받기

dfs(lst, 1, visited_dfs)
