# 현재 위치 입력받고 알파벳으로 정의된 위치를 숫자로 변환하기
st = list(input())
st[0] = ord(st[0])-97
st[1] = int(st[1])-1

# 이동할 간격
directx = [-1, 1, 2, 2, 1, -1, -2, -2]
directy = [-2, -2, -1, 1, 2, 2, 1, -1]

# 이동하기
# 최대로 가능한 경우의 수가 8회이기 때문에 거기서 조건을 충족하지 못하는 경우 cnt를 1씩 깎는 방법을 이용함.
cnt = 8
for i in range(8):
    dx = st[0]+directx[i]
    dy = st[1]+directy[i]
    if dy<0 or dx<0 or dy>8 or dx>8:
        cnt -=1
        continue

print(cnt)