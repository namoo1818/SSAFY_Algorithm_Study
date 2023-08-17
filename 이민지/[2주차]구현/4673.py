# 1부터 10000까지의 정수 리스트
arr = list(range(1,10001))
for n in range(1,10001):
    # 문자열로 바꿔서 각 자리수 더하기
    m = str(n)
    for i in m:
        n+=int(i)
    # 계산한 수가 리스트에 있으면 생성자가 있다는 뜻이니까
    # 리스트에서 제거 
    if n in arr:
        arr.remove(n)
# 리스트에 남은 수는 생성자가 없는 수, 즉 생성자
for i in arr:
    print(i)