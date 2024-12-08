import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

visited = [[False] * m for _ in range(n)]
visited[x][y] = True
dir = d

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def check_neighbors(x,y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if not visited[nx][ny]:
            tmp.append((nx,ny))
            
while True:
    visited[x][y] = True
    tmp = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        

