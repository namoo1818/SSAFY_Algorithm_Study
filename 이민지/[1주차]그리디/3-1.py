n = int(input()) # 거스름돈
cnt = 0 # 총 동전 개수
arr = [500,100,50,10]
for i in arr:
    cnt += n//i # 동전 개수 추가
    n %= i # 남은 거스름돈
print(cnt)