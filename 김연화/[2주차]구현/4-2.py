N = int(input())

count = 0
for i in range(N+1): # 시
  for j in range(60): # 분
    for k in range(60): # 초
      if '3' in str(i)+str(j)+str(k): # 각 단위별로 3이 있다면 카운트 +1 하기
        count +=1

print(count)
