# 6-10
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)
print(*nums)