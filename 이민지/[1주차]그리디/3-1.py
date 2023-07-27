n = int(input())
cnt = n//500
n = n%500
cnt += n//100
n = n%100
cnt += n//50
n = n%50
cnt += n//10
print(cnt)