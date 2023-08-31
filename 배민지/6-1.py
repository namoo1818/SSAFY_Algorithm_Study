# 6-1
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort(start):
    while start < len(arr):        # 인덱스가 배열 길이 안에 있을때
        sorted_arr = sorted(arr)
        # 이미 정렬된 배열 생성(.sort()말고 sorted()를 써서 기존 데이터에 영향이 없도록)
        min_v = sorted_arr[start]   # 최솟값은 정렬된 배열로 부터
        min_idx = arr.index(min_v)  # 최솟값의 기존 배열에서의 인덱스 값
        arr[start], arr[min_idx] = arr[min_idx], arr[start] # 바꿔주기
        print(arr)
        start += 1  # 인덱스 1씩 증가
        if arr == sorted_arr:   # 정렬된 배열과 기존 배열이 같아지면 break
            break

selection_sort(0)   # 0에서 시작