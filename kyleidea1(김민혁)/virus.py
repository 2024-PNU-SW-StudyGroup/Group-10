from collections import deque

com = int(input())
edge = int(input())

graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)

for _ in range(edge):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    graph[s].sort()
    graph[e].sort()

q = deque([1])
cnt = 0

while q:
    v = q.popleft()
    visited[v] = True
    for child in graph[v]:
        if not visited[child]:
            visited[child] = True
            q.append(child)
            cnt += 1

print(cnt)