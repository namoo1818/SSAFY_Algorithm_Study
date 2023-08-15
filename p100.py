N, K = map(int, input().split())
cnt = 0

# N이 K 이상이라면 계속 K로 나누기
while N>=K:
    if N%K==0:
        N = N/K
        cnt +=1
    elif N%K!=0:
        N = N-1
        cnt +=1

# 마지막으로 남은 수에 대하여 1씩 빼기
while N>1:
    N -=1
    cnt+=1

print(cnt)