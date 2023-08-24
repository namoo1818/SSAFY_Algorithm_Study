# 이동할 수 있는 방향
d = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x,y):
    # 방문 처리
    visited[x][y] = True
    # 이동할 수 있는 네 방향을 모두 살펴본다
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        # 이동할 수 있고 얼음이 있고 처음 방문하는거라면
        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0 and not visited[nx][ny]:
            # 이동할 위치를 dfs에 다시 집어넣는다 
            dfs(nx,ny)

# 얼음판 크기 n x m
n,m = map(int,input().split())
# 얼음판 리스트 입력
arr = [list(map(int,input().rstrip())) for _ in range(n)]
# 방문 체크 리스트
visited = [[False]*m for _ in range(n)]
# 아이스크림 개수
ans = 0
# 완전 탐색
for i in range(n):
    for j in range(m):
        # 얼음 부분이고 아직 방문하지 않았다면
        if arr[i][j] == 0 and not visited[i][j]:
            # dfs 돌리고 ans + 1
            dfs(i,j)
            ans+=1
# 답 출력
print(ans)
