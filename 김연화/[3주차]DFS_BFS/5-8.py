def dfs(arr, v,visited):
  #현재노드는 방문!
  visited[v] = True
  print(v,end=' ')
  for i in arr[v]:
    if not visited[i]:
      dfs(arr,i,visited)

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

dfs(arr,1,visited)
