import sys
from collections import deque

input = sys.stdin.readline
r,c  = map(int,input().split())
matrix = [list(input().rstrip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

for row in matrix:
    print(row)

x_list = []
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'D':
            d = (i,j)
            visited[i][j] = True
        elif matrix[i][j] == 'S':
            s = (i,j)
            visited[i][j] = True
        elif matrix[i][j] == '*':
            w = (i,j)
            visited[i][j] = True
        elif matrix[i][j] == 'X':
            x_list.append((i,j))
            visited[i][j] = True

wq = deque([w])
sq = deque([s])

dx = (0,0,-1,1)
dy = (-1,1,0,0)

while wq:
    wx,wy = wq.popleft()
    for i in range(4):
        nwx,nwy = wx+dx[i],wy+dy[i]
        if 0<=nwx<c and 0<=nwy<r and not visited[nwx][nwy]:
            visited[nwx][nwy] = True
            matrix[nwx][nwy] = '*'
            wq.append((nwx,nwy))
    sx,sy = sq.popleft()
    for i in range(4):
        nsx,nsy = sx+dx[i],sy+dy[i]
        if 0<=nsx<c and 0<=nsy<r and not visited[nwx][nwy] and matrix

print(visited)