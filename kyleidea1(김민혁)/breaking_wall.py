from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,wall,visited,graph):

    q = deque()
    q.append((x,y,wall))
    visited[x][y][wall] = 1

    while q:
        x, y, wall = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                q.append((nx,ny,wall))
                visited[nx][ny][wall] = visited[x][y][wall] + 1
            if graph[nx][ny] == 1 and wall == 1:
                q.append((nx,ny,wall-1))
                visited[nx][ny][wall-1] = visited[x][y][wall] + 1
    return -1 

print(bfs(0,0,1,visited,graph))

# from collections import deque
# import sys
# n, m = map(int, input().split())

# mapp = []

# for _ in range(n):
#     row = list(map(int, input()))
#     mapp.append(row)

# q = deque([])


# visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]

# visited[0][0][0] = True
# visited[1][0][0] = True

# q.append((0, 0, 0, 1))

# while q:
#     cx, cy, isBreak, dist = q.popleft()

#     if cx == n-1 and cy==m-1:
#         print(dist)
#         sys.exit()

#     for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#         nx, ny = cx+a, cy+b

#         if 0<=nx<n and 0<=ny<m:
#             if mapp[nx][ny] == 0 and not visited[isBreak][nx][ny]:
#                 visited[isBreak][nx][ny] = True
#                 q.append((nx, ny, isBreak, dist+1))
#             elif mapp[nx][ny] == 1:
#                 if isBreak == 0 and not visited[1][nx][ny]:
#                     visited[1][nx][ny] = True
#                     q.append((nx, ny, 1, dist+1))


# print(-1)