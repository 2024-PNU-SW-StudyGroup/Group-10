from collections import deque
import copy

n, m = map(int, input().split())
matrix = []*m
for _ in range(n):
    l = list(map(int, input().split()))
    matrix.append(l)

zero = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero.append((i,j))
z_len = len(zero)

def bfs(_matrix, z_list):
    matrix = copy.deepcopy(_matrix)
    visited = [[False]*m for _ in range(n)]
    for i,j in z_list:
        matrix[i][j] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                q = deque([(i,j)])
                visited[i][j] = True
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if visited[nx][ny] == False and matrix[nx][ny] == 0:
                            visited[nx][ny] = True # 이 부분 주의.
                            """좌표 갱신 오류: x, y = nx, ny라는 코드는 BFS의 특성을 잘못 사용한 것입니다. 큐에서 좌표를 꺼내온 후에는 다음 방향으로 좌표를 바로 갱신하면 안 됩니다. 대신 각 반복에서 사용되는 좌표를 사용해야 합니다."""
                            q.append((nx,ny))
                            matrix[nx][ny] = 2
    return sum(l.count(0) for l in matrix)
    
z_list = []
safe_list = []
for a in range(z_len):
    for b in range(a+1, z_len):
        for c in range(b+1, z_len):
            z_list = (zero[a],zero[b],zero[c])
            safe = bfs(matrix, z_list)
            safe_list.append(safe)

print(max(safe_list))

