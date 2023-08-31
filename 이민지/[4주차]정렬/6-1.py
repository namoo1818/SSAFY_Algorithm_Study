# 선택 정렬
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 차례대로 바꾸는 방식
# 시간복잡도 O(n^2)
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)