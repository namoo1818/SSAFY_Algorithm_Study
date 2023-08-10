N, M = map(int, input().split())
K = list(map(int, input().split()))

combination = []            # 볼링공 조합

for i in range(N):
    for j in range(i, N):
        if K[i] != K[j]:       # 같은 무게 아닌 경우
            combination.append((K[i], K[j]))
print(len(combination))