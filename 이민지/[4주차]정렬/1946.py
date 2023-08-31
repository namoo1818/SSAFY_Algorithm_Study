t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    ans = 0
    for _ in range(n):
        # a는 서류 순위, b는 면접 순위
        a,b = map(int,input().split())
        arr.append((a,b))
    # 서류 순위순으로 정렬
    arr.sort()
    # 서류 1등 지원자의 면접 순위를 min에 저장
    min = arr[0][1]
    # 서류 순위순으로 정렬했으므로 
    # 해당 지원자는 앞의 지원자보다 항상 서류 순위가 낮다
    # 즉 면접 순위가 앞의 지원자보다 높아야 한다
    for a,b in arr:
        # 면접 순위가 앞 사람보다 높다면
        if b<=min:
            # ans 1 증가
            ans+=1
            # 면접 순위 갱신
            min = b

    # 답 출력
    print(ans)