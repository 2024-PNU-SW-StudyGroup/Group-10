from collections import deque
import sys
input = sys.stdin.readline
INF = 1e9

n, e, k, s = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [INF] * (n+1)

q = deque([s])
distance[s] = 0

while q:
    v = q.popleft()
    for child in graph[v]:
        if distance[child] == INF:  # Only if not visited
            distance[child] = distance[v] + 1
            q.append(child)

ans = [i for i in range(1,n+1) if distance[i] == k] 
if not ans:
    print(-1)
else:
    for a in ans:
        print(a)