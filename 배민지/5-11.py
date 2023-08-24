# 5-11
direction = [(0, 1), (1, 0), (-1, 0), (1, 0)]
def bfs(y, x):
    y = y-1
    x = x-1
    visited = [[0] * M for _ in range(N)]
    queue = []
    queue.append((y, x))
    visited[y][x] = 1

    while queue:
        cy, cx = queue.pop(0)
        if cy == N-1 and cx == M-1:
            return visited[cy][cx]
            # return visited

        for dy, dx in direction:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1 and visited[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = visited[cy][cx] + 1

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
print(bfs(1, 1))