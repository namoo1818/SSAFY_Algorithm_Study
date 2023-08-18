# Queue 선입선출
# 라이브러리 활용
from collections import deque

queue = deque()

queue.append(5) # 5
queue.append(2) # 5-2
queue.append(3) # 5-2-3
queue.append(7) # 5-2-3-7
queue.popleft() # 2-3-7
queue.append(1) # 2-3-7-1
queue.append(4) # 2-3-7-1-4
queue.popleft() # 3-7-1-4

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력
print(list(queue)) # 리스트 변환