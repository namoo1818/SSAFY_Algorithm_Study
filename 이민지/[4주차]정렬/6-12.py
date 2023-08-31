N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort() # 오름차순
B.sort(reverse=True) # 내림차순

for i in range(K):
    # A의 원소가 B의 원소보다 작다면
    if A[i]<B[i]:
        # 스와핑
        A[i], B[i] = B[i], A[i]
    # A의 원소가 B의 원소보다 커진다면
    # 더 바꿀 필요가 없으므로 break
    else:
        break

print(sum(A))