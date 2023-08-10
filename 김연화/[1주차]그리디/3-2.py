n, m, k = map(int,input().split())
n_list = list(map(int,input().split()))
n_list.sort(reverse=True)
max_n = n_list[0]
second = n_list[1]
# 가장 큰 수를 최대 k번 반복할 수 있으니 
# 최대값을 구하려면 최대값을 k번 반복 후 
# 한번 두번째로 큰 값을 더해주는 것을 반복하면 된다.
# 주어진 m을 (k+1)로 나누면 이 반복을 얼마나 할 수 있는지 알 수 있게 된다.
# 그리고 반복후 남은 나머지 또한 최대값을 더할 수 있는 횟수로 카운트가 된다.
# 고로 최대값을 더할 수 있는 횟수는  (m//(k+1))*k+m%(k+1) 번이 된다.
sum = max_n*((m//(k+1))*k+m%(k+1)) + second*(m//(k+1))
print(sum)
