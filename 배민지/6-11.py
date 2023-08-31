# 6-11
N = int(input())
stu_info = [list(input().split()) for _ in range(N)]
stu_info.sort(key=lambda x:x[1])
for stu in stu_info:
    print(stu[0], end=' ')