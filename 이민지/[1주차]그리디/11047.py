n, k = map(int,input().split())
arr = []
ans = 0
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in arr:
    if k>=i:
        ans+=k//i
        k%=i
    if k==0:
        break
print(ans)
