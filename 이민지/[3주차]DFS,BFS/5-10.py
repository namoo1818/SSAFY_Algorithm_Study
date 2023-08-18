dir = [(-1,0),(0,1),(1,0),(0,-1)]

def dfs(x,y):
    arr[x][y] = '1'
    for dx,dy in dir:
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<m and arr[nx][ny]=='0':
            dfs(nx,ny)
    else:
        return
    

n,m = map(int,input().split())
arr = [input() for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] =='0':
            dfs(i,j)
            cnt+=1
print(cnt)