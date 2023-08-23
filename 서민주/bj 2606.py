from collections import deque

com = int(input())
pairs = int(input())
graph = [[] for i in range(com+1)] # 그래프 초기화
visited = [0]*(com+1)     # 방문한 컴퓨터인지 표시
for i in range(pairs):
    a, b = map(int, input().split())
    graph[a]+=[b]           # a에 b 연결
    graph[b]+=[a]           # b에 a 연결 -> 양방향
visited[1] = 1              # 1번 컴퓨터부터 시작이니 방문 표시
Q = deque([1])
while Q:
    c = Q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            Q.append(nx)
            visited[nx]=1
print(sum(visited)-1)
