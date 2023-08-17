import sys
input = sys.stdin.readline
n = int(input())
line=1
while n>line:
    n-=line
    line+=1
# 짝수 라인일 때 : 분자 증가, 분모 감소
if line%2==0:
    a = n
    b = line-n+1
# 홀수 라인일 때 : 분자 감소, 분모 증가
else:
    a = line-n+1
    b = n
print("%d/%d"%(a,b))