# 회전 방향
dir = [(-1,0),(0,1),(1,0),(0,-1)]
n,m = map(int,input().split())
x,y,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
# 시작점 방문 체크
arr[x][y] = 1
# 방문한 칸 수 1 증가
ans = 1
while True:
    # 회전 횟수
    step = 0
    for i in range(4):
        j = (i+d)%4
        nx = x + dir[j][0]
        ny = y + dir[j][1]
        # 이동할 수 있으면 이동
        if nx>=0 and nx<n and ny>=0 and ny<m and arr[nx][ny]==0:
            # 방문 체크
            arr[nx][ny] = 1
            # 현재 위치 갱신
            x=nx
            y=ny
            # 방문한 칸 수 1 증가
            ans += 1
        else:
            step+=1
    # 4번 회전했으면 while문을 나감
    if step==4:
        break
print(ans)
