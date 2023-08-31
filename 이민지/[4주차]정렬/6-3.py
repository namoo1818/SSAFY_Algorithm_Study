# 삽입 정렬
# 두 번째 데이터부터 적절한 위치를 찾아 그 위치에 삽입한다
# 시간복잡도 O(n^2)
# 삽입 정렬은 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다

arr = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(arr)):
    for j in range(i,0,-1): 
        if arr[j] < arr[j-1]: 
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)

