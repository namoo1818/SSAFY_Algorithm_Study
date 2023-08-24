# 5-9.py
from collections import deque
# bfs 메서드 정의
def bfs(arr,start,visited):
  # deque -> 임시 배열 위해
  queue = deque([start])
  # 현재노드는 방문 처리
  visited[start] = True
  # 큐가 빌때까지(False가 될때까지)반복
  while queue:
    v = queue.popleft()
    print(v,end=' ')
  
    for i in arr[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
      
arr = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
visited = [False]*9

bfs(arr,1,visited)
