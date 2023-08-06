"""
최대한 많은 회의를 진행하려면 빨리 끝나는 회의 순서대로 정렬해야 한다.
빨리 끝나야 뒤에 더 많은 회의를 진행할 수 있으니까.
그리고 끝나는 시간이 같다면 더 일찍 시작하는 회의 순서대로 정렬해야 한다.
예를 들어 (1,2), (2,2)인 경우
더 일찍 시작하는 회의 순서대로 정렬하면  (1,2) -> (2,2) 는 가능이지만
(2,2) -> (1,2) 은 불가능이기 때문에
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
ans = 0
arr.sort()
for i in range(n):
    temp = 0
    temp+=1
    while True:
        x,y = arr[i]
        for j in range(i,n):
            if(arr[j][0]>=y):
                temp+=1
                y = arr[j][1]
        else:
            break
    ans=max(ans,temp)
print(ans)
