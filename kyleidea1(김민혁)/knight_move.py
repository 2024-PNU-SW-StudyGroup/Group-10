import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    n = int(input())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((sx,sy,0))
    visited[sx][sy] = True
    
    dx = [2,1,-1,-2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    while q:
        x,y,cnt = q.popleft()
        if x == gx and y == gy:
            return cnt
        for i in range(8):
            nx,ny = x + dx[i], y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))
    
T = int(input())
for _ in range(T):
    print(bfs())