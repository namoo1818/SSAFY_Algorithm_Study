N = int(input())
dir = input().split()
# L = (0, -1), R = (0, 1), U = (-1, 0), D = (1, 0)
def move(dir):                  # 움직이는 함수
    now = 1, 1                  # 현재위치
    for direction in dir:
        y, x = now              # y, x에 현재 좌표 할당
        if direction == 'L':    # L, R, U, D의 경우
            ny, nx = y, x-1     # 각각 방향으로 next y, next x 할당
            if 1 <= ny <= N and 1 <= nx <= N:       # ny, nx가 정사각형 공간 안에 있을 때
                now = ny, nx    # now에 ny, nx 할당
            else:               # 정사각형 공간을 벗어날 때는 반복문 반복
                continue
        elif direction == 'R':
            ny, nx = y, x+1
            if 1 <= ny <= N and 1 <= nx <= N:
                now = ny, nx
            else:
                continue
        elif direction == 'U':
            ny, nx = y-1, x
            if 1 <= ny <= N and 1 <= nx <= N:
                now = ny, nx
            else:
                continue
        elif direction == 'D':
            ny, nx = y+1, x
            if 1 <= ny <= N and 1 <= nx <= N:
                now = ny, nx
            else:
                continue
    for i in now:
        print(i, end=' ')
move(dir)