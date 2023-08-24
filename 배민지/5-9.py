# 5-9
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

def BFS(node, graph):
    visited = [0] * len(graph)
    queue = []
    queue.append(node)
    visited[node] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        for i in graph[now]:
            if i not in queue and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

BFS(1, graph)