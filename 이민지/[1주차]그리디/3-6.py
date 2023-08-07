n, k = map(int,input().split())
ans = 0
while True:
    # n이 k로 나누어떨어지는 수(target)이 될 때까지 1씩 빼기
    # 1씩 뺀 횟수 : n-target
    target = (n//k) * k
    ans += (n-target)
    n = target
    # n이 k보다 작다면 while문 탈출
    if n < k:
        break
    # k로 나누기
    n //= k
    ans +=1
# n이 1이 될 때까지 1씩 빼기
print(ans+(n-1))