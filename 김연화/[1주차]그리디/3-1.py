n = int(input())
count = 0
# while문으로 잔돈이 0이 될때까지만 카운트를 할 수 있게 설정
while n>0:
    # 가장 큰 단위부터 잔돈에서 빼면서 카운트하기
    if n>=500:
        n-=500
        count+=1
    elif n>=100:
        n-=100
        count +=1
    elif n>=50:
        n-=50
        count +=1
    else :
        n-=10
        count +=1
print(count)
