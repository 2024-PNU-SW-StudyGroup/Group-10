from collections import deque

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(matrix):
    q = deque([(0, 0, 0)])  # (x, y, 이동 거리)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while q:
        x, y, dist = q.popleft()

        if x == n - 1 and y == m - 1:
            return dist + 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return -1

min_distance = float('inf')

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            matrix[i][j] = 0
            distance = bfs(matrix)
            if distance != -1:
                min_distance = min(min_distance, distance)
            matrix[i][j] = 1

if min_distance == float('inf'):
    print(-1)
else:
    print(min_distance)
