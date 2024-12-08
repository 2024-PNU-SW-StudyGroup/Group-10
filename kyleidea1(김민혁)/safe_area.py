import sys
import copy

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)

limit = max([max(row) for row in matrix])
visited = [[False]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,rain):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if not visited[nx][ny] and matrix[nx][ny] > rain:
            visited[nx][ny] = True
            dfs(nx,ny,rain)

safety_num = []

for rain in range(limit+1):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > rain and not visited[i][j]:
                dfs(i,j,rain)
                cnt += 1
    safety_num.append(cnt)

print(max(safety_num))

            


    