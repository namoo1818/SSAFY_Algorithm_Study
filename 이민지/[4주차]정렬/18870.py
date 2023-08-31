n = int(input())
arr = list(map(int,input().split()))
# 입력받은 배열을 세트로 바꿔서 중복을 지우고 다시 리스트로 바꿈 그리고 정렬
setArr = sorted(list(set(arr)))
ans = {} # 정답 딕셔너리
for i in range(len(setArr)):
    ans[setArr[i]] = i
# 답 출력
for i in arr:
    print(ans[i], end=' ')