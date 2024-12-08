import sys
from collections import deque
input = sys.stdin.readline

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

def bfs(start):
    q = deque([start])
    visited = set([])
    visited.add(start)

    while q:
        v = q.popleft()
        for child in graph[v]:
            if child not in visited:
                q.append(child)
                visited.add(child)

    return visited

l = [0]*(n+1)
for i in range(1,n+1):
    tmp = bfs(i)
    l[i] += (len(tmp)-1)
    for j in tmp:
        l[j] += 1

print(l.count(n))