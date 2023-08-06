n, k = map(int,input().split())
ans = 0
while(n>1):
    # 1. n을 k로 나누기 : n이 k로 나누어 떨어질 경우에
    if(n%k==0):
        n/=k
    # 2. n에서 1 빼기 : n이 k로 나누어 떨어지지 않을 경우에
    else:
        n-=1
    ans+=1
print(ans)