N = int(input())
arr = [] # 입력 리스트
d = {} # 딕셔너리
most = [] # 최빈값 리스트
# 입력
for _ in range(N):
    i = int(input())
    arr.append(i)
    # 딕셔너리에 없으면 새로 추가
    if not d.get(i):
        d[i] = 1
    # 있으면 개수 증가
    else:
        d[i] += 1

# 오름차순 정렬
arr.sort()

# 1. 산술평균
print(round(sum(arr)/N))

# 2. 중앙값
print(arr[N//2])

# 3. 최빈값
for key, value in d.items():
    # 최빈값이면 최빈값 리스트에 추가
    if value == max(d.values()):
        most.append(key)
# 오름차순 정렬
most.sort()
# 최빈값이 두개 이상이면
if len(most)>1:
    # 두번째로 작은 값 출력
    print(most[1])
else:
    # 하나면 그냥 출력
    print(most[0])
    

# 4. 범위
print(max(arr)-min(arr))