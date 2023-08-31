# 백준 18870 (시간초과ㅠ)
N = int(input())
X = list(map(int, input().split()))
J = set(X)
compact = []
for i in X:
    cnt = 0
    for j in J:
        if j < i:
            cnt += 1
    compact.append(cnt)
print(*compact)