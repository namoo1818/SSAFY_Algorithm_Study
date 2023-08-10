n, m = map(int,input().split())
# 비어있는 리스트 생성
k_list = []
# n개의 행 각각에 리스트를 입력받음
for i in range(n):
    k_list.append(list(map(int,input().split())))
# 각 행에서 가장 작은 수를 넣어줄 리스트 생성
min_list = []
for ks in k_list:
  # 각 행에서 가장 작은수를 앞선 리스트에 추가
    min_list.append(min(ks))
# 리스트에 담긴 수들 중 가장 큰 수를 출력
print(max(min_list))
