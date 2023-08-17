# 입력받는 초기 위치 중 행과 열을 따로 출력해 p_list안에 넣는다
p_list = []
for p in str(input()):
  p_list.append(p)
# 현재 위치에서 
# 좌상향 1, 좌상향2,우상향1,우상향2,좌하향1,좌하향2, 우하향1,우하향2
# 할 때 더해지는 값들을 계산하여 행, 열 리스트에 각각 넣기
dirx = [-2,-1,-2,-1,1,2,1,2]
diry = [-1,-2,1,2,-2,-1,2,1]
# 입력받은 위치값을 int형태로 바꿈
x = int(p_list[1])-1
y = ord(p_list[0])-ord('a')

count = 0
for k in range(8):
  nextx = x+dirx[k]
  nexty = y+diry[k]
  if nextx>=0 and nextx<8 and nexty>=0 and nexty<8:
    count +=1

print(count)
