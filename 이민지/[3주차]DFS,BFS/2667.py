import sys
input = sys.stdin.readline
# 이동할 수 있는 방향
d = [(-1,0),(1,0),(0,-1),(0,1)]
# DFS 깊이 우선 탐색
def dfs(x,y):
    # 한 단지내에 있는 집 수를 cnt로 센다
    global cnt
    # 방문 처리
    visited[x][y] = True
    # cnt 층가
    cnt+=1
    # 네 방향으로 탐색
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        # 만약 이동할 수 있고 처음 방문하는거라면 
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1 and not visited[nx][ny]:
            # 다시 dfs 돌린다
            dfs(nx,ny)
    # cnt 리턴
    return cnt

# 지도의 크기 n
n = int(input())
# 지도 리스트 입력
arr = [list(map(int,input().rstrip())) for _ in range(n)]
# 방문 처리할 리스트
visited = [[False]*n for _ in range(n)]
# 총 단지 수를 저장할 변수 ans
ans = 0
# 각 단지별 집 수를 저장할 리스트 house
house = []
# 지도 리스트 완전 탐색
for i in range(n):
    for j in range(n):
        # 집이 있고 처음 방문하는 곳이라면
        if arr[i][j]==1 and not visited[i][j]:
            # dfs 함수에 집어넣고 단지 수를 1 증가시킨다
            cnt = 0
            house.append(dfs(i,j))
            ans+=1
# 각 단지내 집 수를 오름차순으로 정렬한다
house.sort()
# 총 단지 수 출력
print(ans)
# 각 단지내 집 수 출력
for i in house:
    print(i)

