import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

def one_year_later(ice_matrix):
    cnt_matrix = [[0]*m for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(n):
        for j in range(m):
            if ice_matrix[i][j] != 0:
                for k in range(4):
                    if matrix[i+dx[k]][j+dy[k]] == 0:
                        cnt_matrix[i][j] += 1
    
    for i in range(n):
        for j in range(m):
            ice_matrix[i][j] = ice_matrix[i][j] - cnt_matrix[i][j] if ice_matrix[i][j] - cnt_matrix[i][j] > 0 else 0
    return ice_matrix

def bfs(matrix,i,j):
    bfs_matrix = [row[:] for row in matrix]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 1
    q = deque()
    q.append((i,j))
    bfs_matrix[i][j] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<1 or ny<1 or nx>=n-1 or ny>=m-1:
                continue
            if bfs_matrix[nx][ny] != 0:
                q.append((nx,ny))
                bfs_matrix[nx][ny] = 0
                cnt += 1            
    return cnt

def find_nonzero(matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                return (i,j)
    return -1,-1

year = 0
while True:
    after_matrix = one_year_later(matrix)
    year += 1
    size_of_whole_glacier = sum([len([i for i in row if i != 0]) for row in after_matrix])
    x,y = find_nonzero(after_matrix)
    if x == -1 and y == -1:
        year = 0
        break
    size_of_one_glacier = bfs(after_matrix,x,y)
    if size_of_one_glacier != size_of_whole_glacier:
        break
print(year)