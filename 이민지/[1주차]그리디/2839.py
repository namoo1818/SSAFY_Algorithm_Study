n = int(input())
# 5로 나누어 떨어지면 답 출력
if n%5==0:
    print(n//5)
else:
    # 5키로 봉지가 최대 (n//5)개일 경우부터 하나씩 줄이면서 계산
    for i in range(n//5,-1,-1):
        # 3으로 나누어 떨어지면 답 출력
        if((n-5*i)%3==0):
            print(i+(n-5*i)//3)
            break
    # for-else문 : for문이 break 등으로 끊이지 않고 끝까지 수행되었을 때 else 수행
    # 정확하게 N킬로그램을 만들 수 없을 때 -1 출력
    else:
        print(-1)