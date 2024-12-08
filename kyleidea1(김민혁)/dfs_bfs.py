from collections import deque

n,e,s = map(int, input().split())
graph = [[] for _ in range(n2+1)]
visited_dfs = [s]
visited_bfs = [s]

for i in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, visited_dfs, start):
    for child in graph[start]:
        if child not in visited_dfs:
            print(child, end = ' ')
            visited_dfs.append(child)
            dfs(graph, visited_dfs, child)

print(s, end = ' ')
dfs(graph, visited_dfs, s)
print()
print(s, end = ' ')
q = deque([s])
while q:
    node = q.popleft()
    for child in graph[node]:
        if child not in visited_bfs:
            q.append(child)
            visited_bfs.append(child)
            print(child, end = ' ')
