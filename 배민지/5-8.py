# 5-8
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 8, 6],
    [1, 7]
]


def DFS(node):
    visited[node] = True
    print(node, end = ' ')

    for i in graph[node]:
        if not visited[i]:
            DFS(i)

visited = [False] * len(graph)
DFS(1)