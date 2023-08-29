# p.178 위에서 아래로

n = int(input())
lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

for i in range(n-1):
    for j in range(i+1, n):
        if lst[i]<lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(*lst)