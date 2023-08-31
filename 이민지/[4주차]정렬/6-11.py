N = int(input())
arr = []
for _ in range(N):
    # 이름과 성적 입력
    name, age = input().split()
    # 배열에 저장
    arr.append((name,int(age)))
# 성적 낮은 순으로 정렬(람다 사용)
arr.sort(key = lambda x : x[1])
# 이름 출력
for name, age in arr:
    print(name, end=' ')