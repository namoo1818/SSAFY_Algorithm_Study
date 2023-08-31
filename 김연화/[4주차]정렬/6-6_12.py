#6-6 계수 정렬 소스코드
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]] +=1

for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=' ')

#6-7 sorted 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

#6-8 sort 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

# 6-9 정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
  return data[1]
result = sorted(array, key=setting)
print(result)

# 6-10
n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
  print(i, end=' ')

# 6-11
n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  array.append((input_data[0],int(input_data[1])))

array = sorted(array, key= lambda student : student[1])

for student in array:
  print(student[0],end=' ')

#6-12

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i]<b[i]:
    a[i],b[i] = b[i],a[i]
  else:
    break

print(sum(a))
