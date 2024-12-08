from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            elif graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
    return graph

for t in range(T):
    w,h,B = map(int, input().split())
    graph = [[0]*w for _ in range(h)]
    for b in range(B):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y] == 1:
                cnt += 1
                graph = bfs(graph, x, y)
    print(cnt)

