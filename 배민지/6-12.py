# 6-12
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
for i in range(N):
    if K <= 0:
        break
    else:
        A[i], B[N-1-i] = B[N-1-i], A[i]
        K -= 1
print(sum(A))