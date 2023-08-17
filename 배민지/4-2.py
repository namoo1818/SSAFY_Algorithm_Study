N = int(input())
cnt = 0                         # 3을 포함하는 카운트 초기화
for hr in range(N+1):           # N시 59분 59초 까지이기 때문에 range는 N+1로 설정
    for min in range(60):
        for sec in range(60):
            if '3' in list(str(hr)) or '3' in list(str(min)) or '3' in list(str(sec)):      # 문자열이 '3'을 포함하면 카운트 증가
                cnt += 1
print(cnt)