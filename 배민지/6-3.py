# 6-3
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):       # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            print(arr)
        else:       # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

'''
[5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
[5, 7, 0, 9, 3, 1, 6, 2, 4, 8]
[5, 0, 7, 9, 3, 1, 6, 2, 4, 8]
[0, 5, 7, 9, 3, 1, 6, 2, 4, 8]
[0, 5, 7, 3, 9, 1, 6, 2, 4, 8]
[0, 5, 3, 7, 9, 1, 6, 2, 4, 8]
[0, 3, 5, 7, 9, 1, 6, 2, 4, 8]
[0, 3, 5, 7, 1, 9, 6, 2, 4, 8]
[0, 3, 5, 1, 7, 9, 6, 2, 4, 8]
[0, 3, 1, 5, 7, 9, 6, 2, 4, 8]
[0, 1, 3, 5, 7, 9, 6, 2, 4, 8]
[0, 1, 3, 5, 7, 6, 9, 2, 4, 8]
[0, 1, 3, 5, 6, 7, 9, 2, 4, 8]
[0, 1, 3, 5, 6, 7, 2, 9, 4, 8]
[0, 1, 3, 5, 6, 2, 7, 9, 4, 8]
[0, 1, 3, 5, 2, 6, 7, 9, 4, 8]
[0, 1, 3, 2, 5, 6, 7, 9, 4, 8]
[0, 1, 2, 3, 5, 6, 7, 9, 4, 8]
[0, 1, 2, 3, 5, 6, 7, 4, 9, 8]
[0, 1, 2, 3, 5, 6, 4, 7, 9, 8]
[0, 1, 2, 3, 5, 4, 6, 7, 9, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''