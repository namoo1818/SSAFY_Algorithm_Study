def solution(food_times, k):
    N = len(food_times)
    if set(food_times) == {0}:          # 더 섭취할 음식이 없을 때
        answer = -1
        return answer
    else:
        while sum(food_times) >= 1:     # 섭취할 음식이 있을동안
            max_v = 0                   # 최댓값 초기화
            for j in range(N):          # 음식 갯수만큼 반복
                if max_v <= food_times[j]:
                    max_v = food_times[j]       # 가장 많이 남은 음식이 max_v
                if food_times[j] >= 1:          # 음식이 1 이상 남았을 경우 1 차감
                    food_times[j] -= 1
                if max_v == 1:                  # 가장 많이 남은 음식 양이 1일 경우
                    answer = j+1                # 음식의 인덱스에 1을 더한 값이 음식번호
                    return answer


print(solution([3, 1, 2], 5))