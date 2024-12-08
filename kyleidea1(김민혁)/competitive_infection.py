from collections import deque

N, V = map(int,input().split())
matrix = []
for i in range(N):
    elements = list(map(int, input().split()))
    matrix.append(elements)
s, res_x, res_y  = map(int, input().split())

q = [deque([]) for _ in range(V+1)] # 바이러스별 큐
visited = [[] for _ in range(V+1)] # 바이러스별 방문 목록

for virus in range(1,V+1): # 첫 큐 넣어주고 방문처리까지
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == virus:
                q[virus].append((i,j))
                visited[virus].append((i,j))

def bfs_one_step(matrix,virus,q,visited):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for _ in range(len(q[virus])): # 핵심!!! 한 패스에 큐를 다 비워야 함
        x,y = q[virus].popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if (nx,ny) not in visited[virus]:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = virus
                    visited[virus].append((nx,ny))   
                    q[virus].append((nx,ny))

for _ in range(s):
    for virus in range(1, V+1):
        if q[virus]:
            bfs_one_step(matrix, virus, q, visited)

print(matrix[res_x-1][res_y-1])