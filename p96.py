# 이코테 p96 - 답이 다르게 나오는데요? ㅜ_ㅜ

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 각 행 별로 가장 작은 값의 카드 뽑는 코드 작성하기 - 버블 정렬 이용 - 코드 오류 떠서 수정해야 함
lst_min = [0] * N
for i in range(N): # 각 Y축마다 구할 것이기 때문에 N번 돌림
    for j in range(M-1, 0, -1): # 각 행별로 버블 정렬 이용해서 lst_min에 삽입하기
        for k in range(j):
            if lst[j][k]>lst[j][k+1]:
                lst[j][k], lst[j][k+1] = lst[j][k+1], lst[j][k]
                lst_min.append(lst[j][0])

# 가장 작은 값의 카드끼리 경쟁시켜서 가장 큰 값의 카드 나오게 설정
lst_min_min = 21e8
for i in range(N):
    if lst_min[i]<lst_min_min:
        lst_min_min = lst_min[i]

print(lst_min_min)
