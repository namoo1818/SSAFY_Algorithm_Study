'''
최소경로는 BFS
BFS는 큐로 푼다
visited 리스트를 쓰지 않고 미로 배열 arr에서 방문한 칸 수를 더해서 계산했다
예를 들어 arr[i][j] = num 이면 좌표 (i,j)까지 지나야 하는 최소 방문 칸 수가 num이다

입력
1  0  1  1  1  1
1  0  1  0  1  0
1  0  1  0  1  1
1  1  1  0  1  1

bfs 이후
1  0  9  10 11  12
2  0  8  0  12  0
3  0  7  0  13  14
4  5  6  0  14  15
'''
from collections import deque
import sys
input = sys.stdin.readline
# 이동할 수 있는 방향
d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if(0<=nx<n and 0<=ny<m and arr[nx][ny]==1):
                arr[nx][ny]=arr[x][y]+1
                q.append((nx,ny))
                
n,m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
bfs(0, 0)
# 도착지까지 지나야 하는 최소 칸 수
print(arr[-1][-1])