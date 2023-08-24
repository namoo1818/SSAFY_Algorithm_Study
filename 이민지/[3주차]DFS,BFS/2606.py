# dfs, bfs 둘 다 가능
# dfs로 풀겠다
import sys
input = sys.stdin.readline
def dfs(v,visited):
    global ans
    visited[v] = True
    ans+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

# 컴퓨터의 수
n = int(input())
# 연결선 수
m = int(input())
# 컴퓨터 연결 리스트
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)
# 답 
ans = 0
dfs(1,visited)
# 자기자신은 뺀다
print(ans-1)
