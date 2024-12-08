from collections import deque

n = int(input())
nodes = list(map(int, input().split())) # nodes[0] = -1
start = int(input())

graph = [[] for _ in range(n)]
visited = []

for i in range(n):
    if i != start and nodes[i] != -1:
        graph[nodes[i]].append(i)

q = deque([start])
while q:
    v = q.popleft()
    visited.append(v)
    for child in graph[v]:
        q.append(child)

for node in visited:
    graph[node] = [-1]

print(len(list(filter(lambda x: len(x)==0, graph))))
