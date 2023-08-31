arr = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(arr,key=setting) # 숫자를 기준으로 정렬
print(result)