from collections import deque
import sys
input = sys.stdin.readline

n,l,r = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def bfs(sy,sx):
    q = deque([(sy,sx)])
    visited = set((sy,sx))
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    while q:
        y,x = q.popleft()
        area = []
        area_sum = 0
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            if 0<=ny<n and 1<=nx<n and (nx,ny) not in visited:
                if l <= abs(matrix[ny][nx] - matrix[y][x]) <= r:
                    area.append((ny,nx))
                    area_sum += matrix[ny][nx]
                    visited.add((ny,nx))
    return 

schedule = []

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
print(schedule)
