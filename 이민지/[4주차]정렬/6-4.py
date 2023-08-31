# 퀵 정렬
# 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
# 피벗, 재귀 사용
# 평균 시간복잡도 O(NlogN)
# 최악 시간복잡도 O(N^2) : 이미 정렬되어 있는 경우

arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return 
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 왼쪽으로 이동
        while left <= end and arr[left] <= arr[pivot]:
            left+=1
        # 피벗보다 작은 데이터를 찾을 때까지 오른쪽으로 이동
        while right > start and arr[right] >= arr[pivot]:
            right-=1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)
    
quick_sort(arr,0,len(arr)-1)
print(arr)
