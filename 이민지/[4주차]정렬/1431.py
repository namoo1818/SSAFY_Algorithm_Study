n = int(input())
arr = list(input() for _ in range(n))

def setting(data):
    ans = 0
    for i in data:
        if i.isdigit():
            ans+=int(i)
    return ans

# 사전순으로 정렬
arr.sort(key = lambda x : (len(x), setting(x), x))
print('\n'.join(arr))