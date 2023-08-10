# 애초에 전체를 뒤집을 일이 있나요,,,?
S = list(input())
idx = []
start = S[0]                    # 최초 문자 초기화

for i in range(len(S)):
    if S[i] != start:           # 최초 문자와 다른 문자의 인덱스를
        idx.append(i)           # 빈 리스트에 추가
        start = S[i]            # 그 문자를 최초문자로 설정

# 문자가 바뀌는 지점이 1, 2개->최소횟수 1회 / 3, 4개->최소횟수 2회 이런식으로 진행되어서 이렇게 풀었습니다
if len(idx) % 2 == 1:       # 홀수일 경우 1 더해서 2로 나누어주기
    cnt = (len(idx) + 1) // 2
elif len(idx) % 2 == 0:     # 0 또는 짝수일 경우 2로 나누어주기
    cnt = len(idx) // 2

print(cnt)