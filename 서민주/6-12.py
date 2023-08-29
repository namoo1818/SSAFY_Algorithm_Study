# p183 두 배열의 원소 교체

n, k = map(int, input().split()) # n은 배열의 길이, k는 바꿀 수 있는 횟수
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 정렬하기
a.sort()
b.sort(reverse=True)

# a의 요소와 b의 요소를 바꿔주기
for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))