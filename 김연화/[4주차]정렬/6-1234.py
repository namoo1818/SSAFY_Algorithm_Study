array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index]>array[j]:
      min_index = j
  array[i],array[min_index] = array[min_index],array[i]

print(array)

#6-2.파이썬 스와프(swap) 소스코드
array = [3,5]

array[0],array[1] = array[1],array[0]

print(array)

#6-3.삽입정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i,0,-1):
    if array[j]<array[j-1]:
      array[j],array[j-1] = array[j-1],array[j]
    else:
      break

# print(array)

#6-4.퀵정렬
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
  if start >= end:
    return
  pivot = start
  left = start+1
  right = end
  while left <=right:
    while left <= end and array[left]<=array[pivot]:
      right -=1
    if left>right:
      array[right],array[pivot] = array[pivot],array[right]
    else:
      array[left],array[right] = array[right],array[left]
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)
quick_sort(array,0,len(array)-1)
print(array)
