n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0
# 각 행별로 가장 작은 수를 찾아 ans와 비교
# 이중 for문
for arr2 in arr:
    min_val = 10001
    for i in arr2:
        min_val = min(min_val, i)
    ans = max(ans,min_val)
print(ans)