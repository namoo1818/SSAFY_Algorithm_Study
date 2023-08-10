N = int(input())
fear_list = list(map(int, input().split()))

groups = 0              # 그룹갯수 초기화
ranger = 0              # 그룹 안에 모험가 수 초기화
fear_list.sort()        # 공포도 오름차순으로 fear_list 정렬

for fear in fear_list:
    if fear == 1:       # 공포도가 1이어서 혼자 여행을 갈 수 있는 모험가부터 보내기
        groups += 1
    elif fear > 1:      # 공포도가 같은 모험가 끼리 여행 보내기
        ranger += 1     # ranger 명 수의 연속성을 위해서 fear_list의 sorting이 필요했습니다
                        # (sorting을 안하면 2323일경우 첫번째 3에서 여행을 떠나버리게 됩니다)
        if ranger == fear: # 공포도와 그룹 안 모험가 수가 같아지면
            groups += 1    # 여행 보내기

print(groups)