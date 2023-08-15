n = int(input())
x,y = 1,1
arr = input().split()
for i in arr:
    # 오른쪽
    if i=='R' and y+1<=n:
        y+=1
    # 왼쪽
    if i=='L' and y-1>0:
        y-=1
    # 위
    if i=='U' and x-1>0:
        x-=1
    # 아래
    if i=='D' and x+1<=n:
        x+=1
print(x, y)