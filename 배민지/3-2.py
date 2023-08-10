S = list(map(int, input()))

if S[0] == 0:       # 첫 숫자가 0이면 초기값은 0
    ans = 0
else:               # 아니라면 초기값은 1
    ans = 1

for i in S:
    if i == 0:      # 숫자가 0이면 초기값에 더하기
        ans += i
    else:           # 숫자가 0이 아니면 초기값에 곱하기
        if ans == 0:    # 초기값이 0이라면
            ans = ans + 1   # 초기값에 1 더해주기
        ans *= i

print(ans)