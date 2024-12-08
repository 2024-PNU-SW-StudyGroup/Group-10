import sys
from collections import deque

m,n,k = map(int,input().split())
matrix = [['X']*n for _ in range(m)]

for _ in range(k):
    lx,ly,rx,ry = map(int,input().split())
    w,h = rx-lx,ry-ly
    for i in range(h):
        for j in range(w):
            matrix[ly+i][lx+j] = 'O'

def bfs(x,y):
    cnt = 1
    q = deque([(x,y)])
    matrix[y][x] = 'O'
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if matrix[ny][nx] == 'X':
                q.append((nx,ny))
                matrix[ny][nx] = 'O'
                cnt += 1
    return cnt

q = []
for i in range(n):
    for j in range(m):
        if matrix[j][i] == 'X':
            q.append(bfs(i,j))
q.sort()

print(len(q))
print(*q)