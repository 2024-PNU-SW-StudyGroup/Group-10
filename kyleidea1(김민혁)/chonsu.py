import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
e = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(e):
    c,d = map(int,input().split())
    graph[c].append(d)
    graph[d].append(c)

def bfs(start, target):
    q = deque()
    q.append((start,0))

    while q:
        v,depth = q.popleft()
        if v == target:
            return depth
        for child in graph[v]:
            if not visited[child]:
                visited[child] = True
                q.append((child,depth+1))
    return -1

print(bfs(a,b))