import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    matrix.append(tmp)

mature = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            mature.append((i,j))

def bfs(matrix,mature):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    cnt = 0
    visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    q = []

    for m in mature: # 초기 세팅
        q.append(deque([m]))
        visited[m[0]][m[1]] = True
    
    cnt = 0

    while any(subq for subq in q):
        check = False
        for subq in q:
            for _ in range(len(subq)):
                x, y = subq.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]) or matrix[nx][ny] == -1:
                        continue
                    if matrix[nx][ny] == 0:
                        visited[nx][ny] = True
                        matrix[nx][ny] = 1
                        subq.append((nx,ny))
                        check = True
        if not check:
            break
        else:
            cnt += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return -1
    return cnt

print(bfs(matrix, mature))
