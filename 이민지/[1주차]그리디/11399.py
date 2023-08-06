n = int(input())
# 입력 받은 리스트를 내림차순으로 정렬
arr = sorted(list(map(int,input().split())), reverse=True)
ans = 0
for i in range(n):
    ans += arr[i]*(i+1)
print(ans)
