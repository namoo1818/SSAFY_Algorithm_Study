import sys
input = sys.stdin.readline
# 이동할 수 있는 방향
d = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x,y):
    # 방문 처리
    visited[x][y] = True
    # 이동할 수 있는 네 방향 탐색
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        # 이동할 수 있고 이동하는 땅에 배추가 있고 처음 방문하는거라면 
        if 0<=nx<m and 0<=ny<n and arr[nx][ny] == 1 and not visited[nx][ny]:
            # 다시 dfs로
            dfs(nx,ny)

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    # 배추흰지렁이 마리 수 
    ans = 0
    # 방문 처리 리스트
    visited = [[False]*n for _ in range(m)]
    # 배추밭 리스트
    arr = [[0]*n for _ in range(m)]
    # 배추가 있는 땅을 1로 바꾼다
    for _ in range(k):
        x,y = map(int,input().split())
        arr[x][y] = 1
    # 배추가 있고 처음 방문하는 땅을 찾는다
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                # dfs로 인접한 배추들을 다 방문처리한다
                dfs(i,j)
                # 그리고 ans 1 증가
                ans+=1
    # 답 출력
    print(ans)
