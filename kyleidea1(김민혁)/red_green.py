from collections import deque

n = int(input())
s = []
for i in range(n):
    tmp = input()
    s.append(tmp)

matrix_normal = [[l for l in s[i]] for i in range(n)]
matrix_rg = [['X' if l != 'B' else l for l in s[i]] for i in range(n)]
    
def bfs(matrix):
    visited = [[False] * n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True  # 시작 노드 방문 처리
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        if not visited[nx][ny] and matrix[nx][ny] == matrix[x][y]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt

print(bfs(matrix_normal), bfs(matrix_rg))