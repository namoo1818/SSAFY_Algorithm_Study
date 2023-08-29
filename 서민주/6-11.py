# 성적이 낮은 순서로 학생 출력하기

n = int(input())
arr = []
for i in range(n):
    a, b = input().split()
    b = int(b)
    arr.append([a, b])

for i in range(n-1):
    for j in range(i+1, n):
        if arr[j][1]<arr[i][1]:
            arr[i], arr[j] = arr[j], arr[i]

for i in range(n):
    print(arr[i][0], end=" ")