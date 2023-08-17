# 회전 방향
# 반시계 방향 북 서 남 동
dir = [(-1,0),(0,-1),(1,0),(0,1)]
n,m = map(int,input().split()) # 맵의 크기
x,y,d = map(int,input().split()) # 주인공의 위치 x, y, 바라보고있는 방향 d 0 북쪽
arr = [list(map(int,input().split())) for _ in range(n)] # 맵
visited = [[False] * m for _ in range(n)]
# 시작점 방문 체크
visited[x][y] = True 
# 방문한 칸 수 1 증가
ans = 1 
while True:
    # 회전 횟수
    step = 0
    # 바라보고있는 방향 i = 1
    for i in range(4):
        j = (i+d)%4 # j = 1 동쪽
        nx = x + dir[j][0]
        ny = y + dir[j][1]
        # print("이동전 %d %d %d" %(x, y, j))
        # 이동할 수 있으면 이동
        if nx>=0 and nx<n and ny>=0 and ny<m and arr[nx][ny]==0 and not visited[nx][ny]:
            # 방문 체크
            visited[nx][ny] = True
            # 현재 위치 갱신
            x=nx
            y=ny
            # 바라보고있는 방향 갱신
            d = j
            # 방문한 칸 수 1 증가
            ans += 1
            # print("이동후 %d %d %d" %(x, y, d))
        else:
            step+=1
    
    # 4번 회전했으면 while문을 나감
    if step==4:
        # 뒤로 가기
        nx = x - dir[d][0]
        ny = y - dir[d][1]
        # 뒤가 땅이라서 갈 수 있으면
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        # 갈 수 없으면
        else:
            break
print(ans)