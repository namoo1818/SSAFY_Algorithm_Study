'''
현재 회의 시간이 빨리 끝나야 더 많은 회의를 할 수 있다. 따라서 회의 종료 시간 순으로 정렬한다.
그리고 종료 시간이 같을 경우에는 먼저 시작한 회의를 선택해야 시작 시간과 종료 시간이 같은 회의도 추가할 수 있다.
'''
N = int(input())
ans = 0
time = []
for _ in range(N):
    start, end = map(int,input().split())
    time.append((start, end))
# 1순위 : 종료 시간, 2순위 : 시작 시간
time.sort(key = lambda x : (x[1], x[0]))
ans = 0 # 답
now = 0 # 현재 시간
for s,e in time:
    # 만약 다음 회의 시작 시간이 현재 시간보다 늦거나 같은 경우 추가한다  
    if s>=now:
        ans+=1
        # 시간 갱신
        now = e
print(ans)