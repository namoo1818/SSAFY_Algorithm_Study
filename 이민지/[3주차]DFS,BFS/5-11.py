# 최단거리 문제는 BFS로!
# bfs는 큐 사용
from collections import deque
# 이동할 수 있는 방향
d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
    q = deque()
    # 현재 위치를 큐에 넣음
    q.append((x,y))
    while q:
        # 다시 꺼냄
        x,y = q.popleft()
        # 네 방향 탐색
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            # 만약 이동할 수 있고 처음 방문하는 곳이라면
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                # 이동한 칸은 현재 칸에서 한 칸 더 이동한거니까 +1
                arr[nx][ny] = arr[x][y] + 1
                # q에 이동한 위치 삽입
                q.append((nx,ny))
    # 답 리턴
    return arr[-1][-1]

# 미로 크기 n x m
n,m = map(int,input().split())
# 미로 입력
arr = [list(map(int,input().rstrip())) for _ in range(n)]
# 답 출력
print(bfs(0,0))