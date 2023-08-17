#  x와 y의 위치 기본 설정
x = 1
y = 1
# N*N배열을 위해 N과 방향 전부를 입력받는다
N = int(input())
direction = list(map(str,input().split()))
# 입력받는 direction 이 'U'라면 위로 한칸/'D'라면 아래로 한칸/'R'라면 오른쪽으로 한칸/'L'라면 왼쪽으로 한칸 이동하게 되는 규칙
# 방향 지시대로 움직여야하는데 현재 위치가 이미 가장자리라면 continue로 이동(실행)을 하지 못하게 설정
for d in direction:
    if d=='R':
      if y == N:
          continue
      else:
          y+=1
    elif d=='L':
      if y == 1:
          continue
      else:
          y-=1
    elif d=='U':
      if x == 1:
          continue
      else:
          x-=1

    elif d=='D':
      if x == N:
          continue
      else:
          x += 1
print(x,y)
