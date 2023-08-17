now_j, now_i = input()
now_j = ord(now_j) - 96         # 아스키코드로 변환
now_i = int(now_i)

'''
    LLU = (-1, -2)
    LLD = (1, -2)
    RRU = (-1, 2)
    RRD = (1, 2)
    LDD = (2, -1)
    LUU = (-2, -1)
    RDD = (2, 1)
    RUU = (-2, 1)                                       # 가능한 방향 경우의 수
'''

def move(i, j):
    dir_i = [-1, 1, -1, 1, 2, -2, 2, -2]
    dir_j = [-2, -2, 2, 2, -1, -1, 1, 1]
    cnt = 0                                             # 이동 경우의 수 초기화
    for k in range(8):
        next_i = i + dir_i[k]                           # 지금 i좌표에 방향 더하기
        next_j = j + dir_j[k]                           # 지금 j좌표에 방향 더하기
        if 1 <= next_i <= 8 and 1 <= next_j <= 8:       # 정사각형 안에 있을 때
            cnt += 1                                    # 이동 경우의 수 추가
    return cnt

print(move(now_i, now_j))