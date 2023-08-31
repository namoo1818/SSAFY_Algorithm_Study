# 백준 2018
N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
avg = sum(numbers) / N
mid = numbers[N//2]
cnt_dict = {}
for i in numbers:
    cnt_dict[i] = 0
for i in numbers:
    cnt_dict[i] += 1

for k, v in cnt_dict.items():
    if v == max(cnt_dict.values()):
        frequent = k
        max_cnt = v
temp = []
cnt_list = list(cnt_dict.values())
if cnt_list.count(max_cnt) > 0:
    for k, v  in cnt_dict.items():
        if v == max(cnt_dict.values()):
            temp.append(k)
    temp.sort()
    if len(temp) >= 2:
        frequent = temp[1]

R = numbers[-1] - numbers[0]

print(round(avg))
print(mid)
print(frequent)
print(R)