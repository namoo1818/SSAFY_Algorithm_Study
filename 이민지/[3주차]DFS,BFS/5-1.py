# Stack 선입후출
# 파이썬에서 스택은 리스트를 사용한다
# 별도의 라이브러리 사용 x
stack = []

stack.append(5) # 5
stack.append(2) # 5-2
stack.append(3) # 5-2-3
stack.append(7) # 5-2-3-7
stack.pop() # 5-2-3
stack.append(1) # 5-2-3-1
stack.append(4) # 5-2-3-1-4
stack.pop() # 5-2-3-1

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 리스트 뒤집기 # 최상단 원소부터 출력