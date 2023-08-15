# 이코테 예제 4-1(p111) 상하좌우

# 값 입력받기
n = int(input())
arr = input().split()

# 초기 출발점 설정
y, x = 0, 0

# 이동하기
for i in range(len(arr)):
    if arr[i]=='R':
        x = x+1
    elif arr[i]=='L':
        x = x-1
    elif arr[i]=='U':
        y = y-1
    elif arr[i]=='D':
        y = y+1
    if y<0:
        y = 0
    if x<0:
        x = 0
    if y>=n:
        y = n-1
    if x>=n:
        x = n-1

# 값 도출하기
print(y+1, x+1)