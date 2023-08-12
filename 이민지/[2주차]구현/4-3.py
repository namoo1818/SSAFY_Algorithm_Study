"""
아스키코드 변환 함수
ord(): 문자열 => 아스키코드
chr(): 아스키코드 => 문자열
"""
n =input()
cnt = 0
x = ord(n[0]) - ord('a') + 1
y = int(n[1])
# 이동할 수 있는 경우의 수
dir = [(2,-1),(2,1),(-2,-1),(-2,1),(1,-2),(1,2),(-1,-2),(-1,2)]
for dx, dy in dir:
    nx = x + dx
    ny = y + dy
    # 갈 수 있으면 cnt 증가
    if nx>0 and nx<=8 and ny>0 and ny<=8:
        cnt+=1
print(cnt)