N = int(input())
coins = list(map(int, input().split()))
c = len(coins)

result = []

for i in range(1<<c):       # 이진수를 활용한 부분집합 만들기
    combi = []              # 양의 정수 금액의 모임
    coin_total = 0          # 만들어진 양의 정수 금액
    for j in range(c):
        if i & (1<<j):
            combi.append(coins[j])
            coin_total += coins[j]
    result.append(coin_total)
    result.sort()           # 양의 정수 금액을 오름차순으로 정렬
    my_set = set(result)    # 중복 제거
j = 0
while j >= 0:
    j += 1                  # 1씩 올려가면서 만들어진 양의 정수 금액 중 있는지 확인
    if j not in my_set:
        print(j)
        break