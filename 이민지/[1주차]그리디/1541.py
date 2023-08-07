"""
값을 최소로 만드려면 덧셈을 먼저하고 뺄셈을 마지막에 해야한다.
"""
# -를 기준으로 자르기
arr = list(input().split("-"))
# 처음 -가 나오기 전까지는 무조건 +니까 더하기
temp = list(map(int,arr[0].split("+")))
ans = sum(temp)
for i in arr[1:]:
    # - 기준으로 자른 블록에 해당하는 수 다 더해서 답에서 빼기
    temp = list(map(int,i.split("+")))
    ans-= sum(temp)
print(ans)