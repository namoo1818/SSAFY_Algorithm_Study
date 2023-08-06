n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0
# 각 행별로 가장 작은 수를 찾아 ans와 비교
for i in arr:
    ans = max(ans,min(i))
print(ans)